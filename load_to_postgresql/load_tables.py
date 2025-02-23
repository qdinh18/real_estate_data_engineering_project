from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_data_to_postgresql():
    # List of tuple containing CSV file path and their corresponding target table name
    files_and_tables = [
        ('data_stage/cleaned_data/bds.csv', 'staging_table')  # CSV file for staging_table
    ]
    
    # Define PostgreSQL connection ID for connecting to the database
    postgres_conn_id = 're_connection'

    # Instantiate the PostgresHook to interact with PostgreSQL and get connection and cursor objects
    pg_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = pg_hook.get_conn()  # Establishes a connection to the database
    cursor = conn.cursor()  # Creates a cursor object to execute SQL queries
    
    # Set the date format to European style (DD/MM/YYYY) for date-related queries
    cursor.execute("SET datestyle = 'European, DMY';")
    conn.commit()  # Commit the transaction for setting the datestyle
    
    try:
        # Loop over each CSV file and table pair from the list
        for csv_file, table in files_and_tables:
            with open(csv_file, 'r') as f:  # Open the CSV file for reading
                # Construct the COPY SQL command to efficiently load CSV data into the PostgreSQL table
                copy_sql = f"COPY {table} FROM STDIN WITH CSV HEADER DELIMITER ','"
                # Use the cursor to execute the COPY command, loading data from the file
                cursor.copy_expert(sql=copy_sql, file=f)
            
            conn.commit()  # Commit the data load to the database
            print(f"Loaded data from {csv_file} into {table}.")  # Print a success message for each file

        print("A CSV file has been loaded successfully.")  # Indicate successful completion of data loading

    except Exception as e:
        # Handle any errors that occur during data loading process
        conn.rollback()  # Rollback the transaction to avoid partial data insertion
        print("Error occurred while loading CSV file into PostgreSQL:", e)  # Print the error message
        raise  # Raise the exception to propagate the error

    finally:
        # Ensure that resources (cursor and connection) are properly released after execution
        cursor.close()  # Close the cursor object
        conn.close()  # Close the database connection
