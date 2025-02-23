from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping, RedshiftUserPasswordProfileMapping

from transformation.cleaning_stage import clean_data
from load_to_postgresql.utils_postgres import create_postgres_tables
from load_to_postgresql.load_tables import load_data_to_postgresql
from load_to_s3.upload import upload_csv_to_s3
from load_to_redshift.load_tables import upload_to_redshift, create_redshift_table


default_args = {
    'owner': 'QuyenDinh',
    'start_date': datetime(2025, 2, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes = 1),
    'depends_on_past': False,
}

with DAG(
    dag_id='etl_bds_dag',
    default_args=default_args,
    schedule_interval='0 17 * * *',
    catchup=False,
    max_active_runs=1,
    description='Full ETL DAG with parallel transforms & branching to AWS + local DB'
) as dag:

    start = EmptyOperator(
        task_id='start'

    )

    scrape_task = BashOperator(
        task_id='web_scraping',
        bash_command='scrapy crawl bds -O /opt/airflow/data_stage/raw_data/bds.jsonl',
        cwd='/opt/airflow/web_scraping/web_scraping'

    )

    clean_task = PythonOperator(
        task_id='clean_raw_data',
        python_callable=clean_data

    )

    create_table_in_postgres_task = PythonOperator(
        task_id='create_staging_table_postgresql',
        python_callable=create_postgres_tables

    )

    load_staging_data_task = PythonOperator(
        task_id='load_data_to_postgresql',
        python_callable=load_data_to_postgresql

    )

    postgres_dbt =  DbtTaskGroup(
        group_id="dpostgres_dbt",
        project_config=ProjectConfig("/opt/airflow/real_estate"),
        profile_config=ProfileConfig(
            profile_name="real_estate",
            target_name="dev_postgres",
            profile_mapping=PostgresUserPasswordProfileMapping(
                conn_id="re_connection",
                profile_args={
                    "host": "postgres",
                    "port": 5432,
                    "user": "airflow",
                    "password": "airflow",
                    "dbname": "re",
                    "schema": "public"
                }
            )
        )
    )
    redshift_dbt = DbtTaskGroup(
        group_id="redshift_dbt",
        project_config=ProjectConfig("/opt/airflow/real_estate"),
        profile_config=ProfileConfig(
            profile_name="real_estate",
            target_name="dev_redshift",  # Redshift target
            profile_mapping=RedshiftUserPasswordProfileMapping(
                conn_id="redshift_default",
                profile_args={
                    "host": "quyendinh-redshift-workgroup.841162668345.ap-southeast-2.redshift-serverless.amazonaws.com",
                    "port": 5439,
                    "dbname": "dev",
                    "schema": "public"
                }
            )
        )
    )
    
    upload_to_s3_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_csv_to_s3

    )

    s3_to_redshift_task = PythonOperator(
        task_id='s3_to_redshift',
        python_callable=upload_to_redshift

    )

    create_table_in_redshift_task = PythonOperator(
        task_id='create_tables_in_redshift',
        python_callable=create_redshift_table

    )

    end = EmptyOperator(
        task_id='end'

    )

    # Define task dependencies
    start >> scrape_task >> clean_task
    clean_task >> [create_table_in_postgres_task, create_table_in_redshift_task]
    create_table_in_postgres_task >> load_staging_data_task >> postgres_dbt
    create_table_in_redshift_task >> upload_to_s3_task >> s3_to_redshift_task >> redshift_dbt
    [redshift_dbt, postgres_dbt] >> end
