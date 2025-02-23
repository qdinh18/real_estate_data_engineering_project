# transformation

This directory contains the logic for transforming and processing the data that is scraped from **batdongsan.com**. The transformation process involves only cleaning the data

## Key Component

- **Data Cleaning**: The raw data scraped from the website is cleaned and preprocessed (e.g., removing duplicates, handling missing values).

## Key File

- **cleaning_stage.py**: Handles the cleaning of the scraped data. It processes the raw data and handles data formatting, missing values, and duplicates.

## How to Run

Once the data is scraped and stored in the `data_stage/raw_data/` folder, you can run the following Python scripts to transform the data:

```bash
python cleaning_stage.py
```

These scripts will clean the data, saving the output in the corresponding directory inside `data_stage/`.



