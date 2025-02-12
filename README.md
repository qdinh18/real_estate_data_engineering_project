# Real Estate ETL Pipeline

This project implements a full ETL pipeline for real estate data using **Apache Airflow**. The pipeline scrapes data from the **batdongsan.com** website, processes it, and loads it into multiple storage destinations, including **PostgreSQL**, **AWS S3**, and **AWS Redshift**.

## Project Structure

```plaintext
airflow_dag/           # Contains the Airflow DAG for orchestrating the ETL workflow
├── dag.py
├── data_stage/        # Stores raw and processed data outputs
├── load_to_postgresql/ # Handles PostgreSQL table creation and data loading
├── load_to_redshift/   # Loads data from S3 to Redshift
├── load_to_s3/         # Uploads processed data to AWS S3
├── transformation/      # Contains transformation logic for cleaning and processing data
├── web_scraping/        # Contains Scrapy web scraping logic to extract data
.env                   # Environment configuration (ignored in Git)
docker-compose.yaml    # Docker Compose configuration
requirements.txt       # Python dependencies for the project
README.md              # Project overview and instructions
.gitignore             # Git ignore file
```

## Technologies Used

- **Apache Airflow**: Orchestrates and manages the ETL pipeline.
- **Scrapy**: Framework for scraping real estate data from **batdongsan.com**.
- **PostgreSQL**: Stores processed data for further analysis.
- **AWS S3**: Stores raw and processed data.
- **AWS Redshift**: Data warehouse for high-performance analytics.

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











![Screenshot 2025-02-11 at 21 51 47](https://github.com/user-attachments/assets/8b0bd289-7292-49a9-8f19-c46a8f4f7783)



















## Architecture















![Screenshot 2025-02-11 at 21 39 46](https://github.com/user-attachments/assets/49e01dd9-e32e-41eb-8605-c707dca18bdf)









