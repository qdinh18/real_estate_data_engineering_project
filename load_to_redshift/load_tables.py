from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
import os
from datetime import date  # Import date to work with dates

def upload_to_redshift():
    # Get S3 bucket name from environment variable
    bucket_name = os.getenv('my_bucket')  # Get S3 bucket name from environment variable 
    
    today_date = date.today().strftime('%Y-%m-%d')
    # Define S3 object keys (file names in S3)
    s3_key = [
        f'staging_table_{today_date}.csv'
    ]
    # Define the corresponding Redshift table names
    redshift_tables = [
        'staging_table',  # Target table for staging_table data
    ]
    
    # Instantiate the RedshiftSQLHook to interact with Redshift
    redshift_hook = RedshiftSQLHook(aws_conn_id='redshift_default', schema='public')  # Use appropriate AWS connection and schema
    
    # Loop through each pair of S3 key and Redshift table
    for s3_key, table in zip(s3_key, redshift_tables):
        # Construct the COPY command to load data from S3 into the corresponding Redshift table
        copy_sql = f"""
        COPY {table}
        FROM 's3://{bucket_name}/{s3_key}'
        IAM_ROLE 'arn:aws:iam::841162668345:role/redshift-to-s3-role'  
        CSV IGNOREHEADER 1;
        """
        
        # Execute the COPY command using the RedshiftSQLHook's run method
        redshift_hook.run(copy_sql)
        # Print a success message for each file loaded
        print(f"Data loaded into Redshift table {table} from s3://{bucket_name}/{s3_key}")

def create_redshift_table():
    redshift_hook = RedshiftSQLHook(aws_conn_id='redshift_default')

    redshift_hook.run("""DROP TABLE IF EXISTS dim_broker, dim_post, dim_project, fact_all_apartment CASCADE;""")

    redshift_hook.run("""
    CREATE TABLE IF NOT EXISTS staging_table (
        title           TEXT,
        price_per_m²    FLOAT,
        project_name    TEXT,
        address         TEXT,
        price           FLOAT,
        area            FLOAT,
        bedroom         FLOAT,
        bathroom        FLOAT,
        url             TEXT,
        posted_date     DATE,
        expired_date    DATE,
        project_status  TEXT,
        investor        TEXT,
        broker_name     TEXT,
        broker_rank     TEXT,
        project_area_range     TEXT,
        number_of_apartments   FLOAT,
        number_of_buildings    FLOAT,
        update_date     DATE NOT NULL
    );
    """)
