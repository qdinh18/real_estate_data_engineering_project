# Load_to_postgresql

This directory contains the logic for creating tables in **PostgreSQL** and loading the transformed data into these tables. The transformed data (dimension tables and fact tables) is loaded into a **PostgreSQL** database for further analysis, querying, and storage.

## Key Files

- **create_tables.py**: This Python script uses the `PostgresHook` to connect to PostgreSQL, read the SQL queries from the **`create_tables.sql`** file, and execute them to create the necessary tables.
- **create_tables.sql**: This SQL script contains the table creation queries used by the **`create_tables.py`** script to create the schema and tables in PostgreSQL.
- **load_tables.py**: This script handles loading the cleaned and transformed data into the corresponding PostgreSQL tables. It ensures that the data is correctly inserted into the database after the schema is created.

## Process Overview

1. **Table Creation**: The `create_tables.py` script automates the table creation process by executing the SQL queries from the `create_tables.sql` file using **`PostgresHook`**.
2. **Data Loading**: Once the tables are created, the `load_tables.py` script loads the transformed data (from the `data_stage/` directory) into the appropriate tables in PostgreSQL.

## How to Run

After the transformation scripts have been executed and the data is ready, you can perform the following steps to load the data into PostgreSQL:

1. **Create the Tables**:
   - To create the tables, run the **Python script** that uses the `PostgresHook` to execute the SQL queries:
     ```bash
     python create_tables.py
     ```

2. **Load the Transformed Data**:
   ```bash
   python load_tables.py
   ```

The data will then be available in your PostgreSQL database for querying, reporting, and further analysis.
