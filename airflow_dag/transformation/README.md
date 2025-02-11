# Transformation

This directory contains the logic for transforming and processing the data that is scraped from **batdongsan.com**. The transformation process involves cleaning the data, creating dimension tables, and generating a fact table.

## Key Components

- **Data Cleaning**: The raw data scraped from the website is cleaned and preprocessed (e.g., removing duplicates, handling missing values).
- **Dimensional Modeling**: The data is used to create dimension tables (broker, project, post) that store the metadata related to real estate listings.
- **Fact Table**: A fact table for apartments is created by selecting and aggregating relevant columns from the cleaned data.

## Key Files

- **stage_1_clean.py**: Handles the cleaning of the scraped data. It processes the raw data and handles data formatting, missing values, and duplicates.
- **stage_2_create_dim.py**: Creates the dimension tables (broker, project, post) from the cleaned data.
- **stage_3_create_fact.py**: Creates the fact table for apartments, which aggregates the relevant data for analysis.

## How to Run

Once the data is scraped and stored in the `data_stage/raw_data/` folder, you can run the following Python scripts to transform the data:

```bash
python stage_1_clean.py
python stage_2_create_dim.py
python stage_3_create_fact.py
```

These scripts will clean the data, create the dimension tables, and generate the fact table, saving the outputs in the corresponding directories inside `data_stage/`.



