# web_scraping

This directory contains the Scrapy spider used to scrape data from the **batdongsan.com** website. Scrapy is used here in combination with **curl_cffi** for HTTP requests to avoid being blocked by the website.

## Functionality

- **Scraping Logic**: The spider scrapes real estate data (such as apartment listings, prices, locations, and details) from the **batdongsan.com** website.
- **Data Storage**: The scraped data is saved as **JSONL** format in the `data_stage/raw_data/` folder, which is later used in the ETL pipeline for further processing and transformation.

## Key Files

- **bds.py**: Contains the main logic for scraping the data using **Scrapy** and **curl_cffi** to bypass blocking mechanisms from the website.
- **settings.py**: Contains Scrapy settings for scraping configuration (e.g., request headers, crawl delay).

## How to Run

1. Ensure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

2. To run the scraper manually:
   ```bash
   scrapy crawl bds -O /opt/airflow/airflow_dag/data_stage/raw_data/bds.jsonl
   ```

   This will scrape the data and output it to the `data_stage/raw_data` folder.