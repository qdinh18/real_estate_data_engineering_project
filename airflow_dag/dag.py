from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from transformation.stage_1_clean import clean_data
from transformation.stage_2_create_dim import create_dim_broker, create_dim_project, create_dim_post
from transformation.stage_3_create_fact import create_fact_all_apartment
from load_to_postgresql.utils_postgres import create_tables
from load_to_postgresql.load_tables import load_data_to_postgresql
from load_to_s3.upload import upload_csv_to_s3
from load_to_redshift.load_tables import upload_to_redshift

default_args = {
    'owner': 'QuyenDinh',
    'start_date': datetime(2025, 2, 4),
    'retries': 1,
    'retry_delay': timedelta(minutes = 1),
    'depends_on_past': False
}

dag = DAG(
    dag_id='etl_bds_dag',
    default_args=default_args,
    schedule_interval='0 17 * * *',
    catchup=False,
    max_active_runs = 1,
    description='Full ETL DAG with parallel transforms & branching to AWS + local DB'
    )

start = EmptyOperator(task_id='start',
                      dag = dag)


scrape_task = BashOperator(
    task_id='web_scraping',
    bash_command='scrapy crawl bds -O /opt/airflow/airflow_dag/data_stage/raw_data/bds.jsonl',
    cwd='/opt/airflow/web_scraping/web_scraping',
    dag=dag
)
clean_task = PythonOperator(
    task_id='clean_raw_data',
    python_callable=clean_data,
    dag=dag
)
create_dim_broker_task = PythonOperator(task_id = 'create_dim_broker',
                                        python_callable = create_dim_broker,
                                        dag = dag
)
create_dim_project_task = PythonOperator(task_id = 'create_dim_project',
                                         python_callable = create_dim_project,
                                         dag = dag
)
create_dim_post_task = PythonOperator(task_id = 'create_dim_post',
                                      python_callable = create_dim_post,
                                      dag = dag
)
create_fact_all_apartment_task = PythonOperator(task_id = 'create_fact_all_apartment',
                                                python_callable = create_fact_all_apartment,
                                                dag = dag
)
create_tables_task = PythonOperator(task_id = 'create_fact_and_dim_tables',
                                    python_callable = create_tables,
                                    dag = dag
)
load_data_task = PythonOperator(task_id = 'load_all_tables_to_postgresql',
                                    python_callable = load_data_to_postgresql,
                                    dag = dag
)
upload_to_s3_task = PythonOperator(task_id = 'upload_to_s3',
                                   python_callable=upload_csv_to_s3, 
                                   dag=dag
)
upload_to_redshift_task = PythonOperator(task_id = 's3_to_redshift',
                                   python_callable=upload_to_redshift, 
                                   dag=dag
)
end = EmptyOperator(task_id='end',
                    dag = dag
)
 

start >> scrape_task >> clean_task 
clean_task >> [create_dim_broker_task, create_dim_project_task, create_dim_post_task] 
[create_dim_broker_task, create_dim_project_task, create_dim_post_task] >> create_fact_all_apartment_task 
create_fact_all_apartment_task >> create_tables_task
create_tables_task >> [load_data_task, upload_to_s3_task]
[load_data_task, upload_to_s3_task] >> upload_to_redshift_task
upload_to_redshift_task >> end