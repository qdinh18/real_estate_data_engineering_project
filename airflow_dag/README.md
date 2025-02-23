

# Real Estate ETL Pipeline

Automated workflow for scraping, processing, and loading real estate data to PostgreSQL and Redshift with dbt transformations.

## Workflow Overview


    start-->scrape-->clean
    clean-->create_pg[Create PG Tables]
    clean-->create_rs[Create RS Tables]
    create_pg-->load_pg-->dbt_pg[PG dbt]
    create_rs-->upload_s3-->load_rs-->dbt_rs[RS dbt]
    dbt_pg & dbt_rs-->end


## Key Tasks

| Task | Description | Target |
|------|-------------|--------|
| `web_scraping` | Scrape property data using Scrapy | JSONL |
| `clean_raw_data` | Validate/normalize data | Python |
| `load_data_to_postgresql` | Load to local PostgreSQL | PG |
| `upload_to_s3` | Stage data in S3 | AWS |
| `s3_to_redshift` | Load to Redshift | RS |
| `*_dbt` | Transform data with dbt | Both |

## Requirements

- Airflow 2.6+, PostgreSQL, Redshift, S3
- Python packages: `apache-airflow`, `scrapy`, `dbt`, `cosmos`
- Airflow connections: PostgreSQL, Redshift, AWS

## Setup

 Configure connections in Airflow:
   - PostgreSQL: `re_connection`
   - Redshift: `redshift_default`


## Execution

- **Schedule**: Daily @ 17:00 UTC
- **Run manually**: `airflow dags trigger etl_bds_dag`
- **Test task**: `airflow tasks test etl_bds_dag [task_id] [date]`

## Data Quality

- Built-in dbt tests (not_null, unique)
- Airflow retries (1 retry on failure)
- Schema validation during loading

```

This version keeps essential information while reducing technical details. It focuses on the core workflow, requirements, and key execution commands.
