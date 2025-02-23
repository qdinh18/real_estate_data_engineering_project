# data_stage

This directory stores all the intermediate and output data at different stages of the ETL pipeline.

## Subfolders

- **raw_data**: This folder contains the raw data that is scraped from **batdongsan.com**. The data is stored in **JSONL** format.
- **cleaned_data**: This folder contains the cleaned data after processing it through the **cleaning_stage.py** script.

The data in these folders is sequentially passed through the ETL pipeline, being cleaned, transformed, and loaded into PostgreSQL, S3, and Redshift.

## Workflow

- **Raw Data**: The raw data is scraped using **Scrapy** and stored in the `raw_data` folder.
- **Cleaned Data**: The raw data is cleaned using the **transformation/cleaning_stage.py** script and saved in the `cleaned_data` folder.
