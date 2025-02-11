import pandas as pd
import os
from datetime import date
# Create the fact table
def create_fact_all_apartment():
    dim_broker = pd.read_csv('airflow_dag/data_stage/dim_tables/dim_broker.csv')
    dim_project = pd.read_csv('airflow_dag/data_stage/dim_tables/dim_project.csv')
    dim_post = pd.read_csv('airflow_dag/data_stage/dim_tables/dim_post.csv')
    df = pd.read_csv('airflow_dag/data_stage/cleaned_data/bds.csv')
    # Merge to get broker_id
    df['update_date'] = (date.today()).strftime('%Y-%m-%d')
    df = df.merge(dim_broker, how='left', on=['broker_name', 'update_date'])
    # Merge to get project_id
    df = df.merge(dim_project, how='left', on=['project_name', 'investor', 'project_area_range', 
                                               'project_status', 'address', 'number_of_apartments', 
                                               'number_of_buildings', 'update_date'])
    # Merge to get post_id
    df = df.merge(dim_post, how='left', on=['title', 'url', 'update_date'])

    df['price_unit'] = 'tỷ đồng'
    df['price_per_m²_unit'] = 'triệu đồng'
    df['area_unit'] = 'm²'

    fact_all_apartment = df[
        [
            'post_id',
            'update_date',
            'broker_id',
            'project_id',
            'price',
            'price_unit',
            'price_per_m²',
            'price_per_m²_unit',
            'area',
            'area_unit',
            'bedroom',
            'bathroom'
        ]
    ]

    fact_all_apartment.to_csv('airflow_dag/data_stage/fact_table/fact_all_apartment.csv', index=False, header=True)
 
