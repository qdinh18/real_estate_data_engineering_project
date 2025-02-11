from airflow.providers.postgres.hooks.postgres import PostgresHook

def create_tables():
    # Instantiate the PostgresHook to interact with PostgreSQL
    pg_hook = PostgresHook(postgres_conn_id = 're_connection')

    # Open the SQL file containing the table creation queries and read its contents
    with open('airflow_dag/load_to_postgresql/create_tables.sql', 'r') as file:
        sql_queries = file.read()  # Read all SQL queries from the file

    # Execute the SQL queries using the PostgresHook's run method
    pg_hook.run(sql_queries)
