# load_to_postgresql

This directory contains the logic for creating tables in **PostgreSQL** and loading the transformed data into these tables. The transformed data (dimension tables and fact tables) is loaded into a **PostgreSQL** database for further analysis, querying, and storage.

## Key Files

- **utils_postgres.py**: This Python script uses the `PostgresHook` to connect to PostgreSQL, read the SQL queries from the **`create_staging_table.sql`** file, and execute them to create the necessary tables.
- **create_staging_table.sql**: This SQL script contains the table creation query used by the **`utils_postgres.py`** script to create the staging_table in PostgreSQL.
- **load_tables.py**: This script handles loading the cleaned and transformed data into the staging PostgreSQL table. It ensures that the data is correctly inserted into the database.

## Process Overview

1. **Table Creation**: The `utils_postgres.py` script automates the table creation process by executing the SQL queries from the `create_staging_table.sql` file using **`PostgresHook`**.
2. **Data Loading**: Once the table is created, the `load_tables.py` script loads the transformed data (from the `data_stage/` directory) into the appropriate table in PostgreSQL.

## How to Run

After the transformation scripts have been executed and the data is ready, you can perform the following steps to load the data into PostgreSQL:

1. **Create the Tables**:
   - To create the table, run the **Python script** that uses the `PostgresHook` to execute the SQL queries:
     ```bash
     python utils_postgres.py
     ```

2. **Load the Transformed Data**:
   ```bash
   python load_tables.py
   ```

The data will then be available in your PostgreSQL database for querying, reporting, and further analysis.
