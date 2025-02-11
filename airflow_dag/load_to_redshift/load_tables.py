from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
import os
from datetime import date  # Import date to work with dates

def upload_to_redshift():
    # Get S3 bucket name from environment variable
    bucket_name = os.getenv('bucket_name')  # Get S3 bucket name from environment variable 
    
    today_date = date.today().strftime('%Y-%m-%d')
    # Define S3 object keys (file names in S3)
    s3_keys = [
        f'dim_broker_{today_date}.csv',
        f'dim_post_{today_date}.csv',
        f'dim_project_{today_date}.csv',
        f'fact_all_apartment_{today_date}.csv'
    ]
    # Define the corresponding Redshift table names
    redshift_tables = [
        'dim_broker',  # Target table for dim_broker data
        'dim_post',  # Target table for dim_post data
        'dim_project',  # Target table for dim_project data
        'fact_all_apartment'  # Target table for fact_all_apartment data
    ]
    
    # Instantiate the RedshiftSQLHook to interact with Redshift
    redshift_hook = RedshiftSQLHook(aws_conn_id='redshift_default', schema='public')  # Use appropriate AWS connection and schema
    
    # Loop through each pair of S3 key and Redshift table
    for s3_key, table in zip(s3_keys, redshift_tables):
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
