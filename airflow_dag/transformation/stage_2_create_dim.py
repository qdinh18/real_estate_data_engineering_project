import pandas as pd  # Import pandas for data handling
import os  # Import os for file operations
from datetime import date  # Import date to get today's date

def create_dim_broker():
    # Load cleaned data
    df = pd.read_csv('airflow_dag/data_stage/cleaned_data/bds.csv')

    # Extract unique brokers and assign IDs
    dim_broker = df[['broker_name', 'broker_rank']].drop_duplicates().reset_index(drop=True)
    dim_broker['broker_id'] = dim_broker.index + 1  # Assign unique broker ID
    dim_broker['update_date'] = date.today().strftime('%Y-%m-%d')  # Add update date

    # Rearrange column order
    dim_broker = dim_broker[['broker_id', 'update_date', 'broker_name', 'broker_rank']]

    # Save to CSV
    file_path = 'airflow_dag/data_stage/dim_tables/dim_broker.csv'
    dim_broker.to_csv(file_path, index=False, header=True)
    print(f"Created {file_path} with header.")


def create_dim_project():
    # Load cleaned data
    df = pd.read_csv('airflow_dag/data_stage/cleaned_data/bds.csv')

    # Extract unique projects and assign IDs
    dim_project = df[['project_name', 'investor', 'project_area_range', 'project_status', 
                      'address', 'number_of_apartments', 'number_of_buildings']].drop_duplicates().reset_index(drop=True)
    dim_project['project_id'] = dim_project.index + 1  # Assign unique project ID
    dim_project['update_date'] = date.today().strftime('%Y-%m-%d')  # Add update date

    # Rearrange column order
    dim_project = dim_project[['project_id', 'update_date', 'project_name', 'investor', 
                               'project_area_range', 'project_status', 'address', 
                               'number_of_apartments', 'number_of_buildings']]

    # Save to CSV
    file_path = 'airflow_dag/data_stage/dim_tables/dim_project.csv'
    dim_project.to_csv(file_path, index=False, header=True)
    print(f"Created {file_path} with header.")
    

def create_dim_post():
    # Load cleaned data
    df = pd.read_csv('airflow_dag/data_stage/cleaned_data/bds.csv')
    
    # Convert 'posted_date' and 'expired_date' from dd/mm/yyyy to yyyy-mm-dd
    df['posted_date'] = pd.to_datetime(df['posted_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    df['expired_date'] = pd.to_datetime(df['expired_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    
    # Extract unique posts and assign IDs
    dim_post = df[['title', 'url', 'posted_date', 'expired_date']].drop_duplicates().reset_index(drop=True)
    dim_post['post_id'] = dim_post.index + 1  # Assign unique post ID
    dim_post['update_date'] = date.today().strftime('%Y-%m-%d')  # Add update date

    # Rearrange column order
    dim_post = dim_post[['post_id', 'update_date', 'title', 'url', 'posted_date', 'expired_date']]

    # Save to CSV
    file_path = 'airflow_dag/data_stage/dim_tables/dim_post.csv'
    dim_post.to_csv(file_path, index=False, header=True)
    print(f"Created {file_path} with header.")

