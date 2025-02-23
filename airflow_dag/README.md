# Real Estate ETL Pipeline

This project implements a full ETL pipeline for real estate data using **Apache Airflow**, **Data build tool** (Astronomer Cosmos). The pipeline scrapes data from the **batdongsan.com** website, processes it by using python and dbt, and loads it into multiple storage destinations, including **PostgreSQL**, **AWS S3**, and **AWS Redshift**.

## Architecture

![Screenshot 2025-02-23 at 14 17 00](https://github.com/user-attachments/assets/27f05673-5f54-4f41-a0d5-2726e5644fa0)



## Project Structure

```plaintext
├── airflow_dag/           # Contains the Airflow DAG for orchestrating the ETL workflow
├── data_stage/          # Stores raw and processed data outputs
├── load_to_postgresql/  # Handles PostgreSQL table creation and data loading
├── load_to_redshift/    # Loads data from S3 to Redshift
├── load_to_s3/          # Uploads processed data to AWS S3
├── transformation/      # Contains transformation logic for cleaning and processing data
├── web_scraping/        # Contains Scrapy web scraping logic to extract data
├── real_estate/         # Data build tool project
├── .env                   # Environment configuration (ignored in Git)
├── docker-compose.yaml    # Docker Compose configuration
├── requirements.txt       # Python dependencies for the project
├── README.md              # Project overview and instructions
├── .gitignore             # Git ignore file
```

## Technologies Used

- **Apache Airflow**: Orchestrates and manages the ETL pipeline.
- **Scrapy**: Framework for scraping real estate data from **batdongsan.com**.
- **PostgreSQL**: Stores processed data for further analysis.
- **AWS S3**: Stores raw and processed data.
- **AWS Redshift**: Data warehouse for high-performance analytics.
- **Cosmos**:**Data build tool**: Data model and data quality.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Start the project using Docker Compose:
   ```bash
   docker-compose up
   ```

3. Access the Airflow web UI to monitor DAGs and tasks.

## Data Model


![412044060-8b0bd289-7292-49a9-8f19-c46a8f4f7783](https://github.com/user-attachments/assets/6186ad53-6806-4f54-8db5-1c9106e81b5b)

