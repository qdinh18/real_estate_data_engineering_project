from airflow.providers.postgres.hooks.postgres import PostgresHook

pg_hook = PostgresHook(postgres_conn_id = 're_connection')

def create_postgres_tables():
    # Open the SQL file containing the table creation queries and read its contents
    with open('load_to_postgresql/create_staging_table.sql', 'r') as file:
        sql_queries = file.read()  # Read all SQL queries from the file

    # Execute the SQL queries using the PostgresHook's run method
    pg_hook.run(sql_queries)
