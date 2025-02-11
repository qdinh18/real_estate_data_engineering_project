# Data_stage

This directory stores all the intermediate and output data at different stages of the ETL pipeline.

## Subfolders

- **raw_data**: This folder contains the raw data that is scraped from **batdongsan.com**. The data is stored in **JSONL** format.
- **cleaned_data**: This folder contains the cleaned data after processing it through the **stage_1_clean.py** script.
- **dim_tables**: Contains the dimension tables (broker, project, post) that are created after transforming the cleaned data.
- **fact_table**: Contains the fact table for apartments, generated from the transformed data.

The data in these folders is sequentially passed through the ETL pipeline, being cleaned, transformed, and loaded into PostgreSQL, S3, and Redshift.

## Workflow

- **Raw Data**: The raw data is scraped using **Scrapy** and stored in the `raw_data` folder.
- **Cleaned Data**: The raw data is cleaned using the **transformation/stage_1_clean.py** script and saved in the `cleaned_data` folder.
- **Dimension Tables**: After transformation, the cleaned data is used to create the dimension tables (broker, project, post), and the results are saved in the `dim_tables` folder.
- **Fact Table**: The fact table for apartments is created from the cleaned and transformed data and saved in the `fact_table` folder.
