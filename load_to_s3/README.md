# load_to_s3

This directory contains the logic for uploading processed data to **AWS S3**. After the data is cleaned

and transformed, it is stored in **S3** for further processing or backup. The data in S3 is also used as the source for loading into **Redshift**.

## Key Script

- **upload.py**: This script is responsible for uploading cleaned and transformed data from local storage to **AWS S3**. It works with the output files from the transformation stage (dimension and fact tables).

## Process Overview

1. The data from **data_stage/cleaned_data/**, **data_stage/dim_tables/**, and **data_stage/fact_table/** is uploaded to the corresponding S3 bucket.
2. The data uploaded to S3 can then be used in downstream systems like **Redshift** or other analytics platforms.

## How to Run

After the transformation scripts have been executed and the data is ready, you can use the following script to upload the data to **S3**:

```bash
python upload.py
```

This will upload all the necessary files from the local directory to S3, where they will be available for analysis or loading into Redshift.
