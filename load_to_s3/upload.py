from airflow.providers.amazon.aws.hooks.s3 import S3Hook  # Import S3Hook for AWS S3 operations
import os  # Import os to access environment variables
from datetime import date  # Import date to work with dates

def upload_csv_to_s3():
    # Get S3 bucket name from environment variable
    bucket_name = os.getenv('my_bucket')  # Get S3 bucket name from environment variable

    today_date = (date.today()).strftime('%Y-%m-%d') 
    # Define S3 object keys (file names in S3)
    s3_key = [
        f'staging_table_{today_date}.csv'
    ]

    # Define corresponding local file paths
    file_paths = [
        'data_stage/cleaned_data/bds.csv'
    ]
    
    # Initialize S3Hook with Airflow connection ID
    s3_hook = S3Hook(aws_conn_id='re_connection2')  

    # Iterate through file paths and corresponding S3 keys
    for file, key in zip(file_paths, s3_key):
        s3_hook.load_file(
            filename=file,  # Local file path
            bucket_name=bucket_name,  # Target S3 bucket
            key=key,  # S3 object key (destination filename)
            replace=False  # Prevent overwriting existing files in S3
        )
        print(f"Uploaded {file} to s3://{bucket_name}/{key}")  # Print success message