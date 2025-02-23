# load_to_redshift

This directory contains the logic for uploading data from **AWS S3** to **AWS Redshift**. The transformation and cleaning processes store the data in S3, and this directory handles loading that data into Redshift for further analysis and querying.

## Key Script

- **load_tables.py**: This script handles the uploading of data from **S3** to **Redshift**. It assumes that the data has already been uploaded to S3 and is ready for import into Redshift.

## Process Overview

1. The **`load_to_s3/`** folder uploads the processed data to **AWS S3**.
2. **`load_to_redshift/`** takes over by loading the data stored in S3 into **AWS Redshift** for analysis and reporting. After that, droping all tables in the model is for refreshing purpose, then create the staging_table.

## How to Run

After uploading the processed data to **S3**, you can run the following script to load data into Redshift:

```bash
python load_tables.py
```

This script will load the data from the designated S3 bucket to Redshift for further analysis.
