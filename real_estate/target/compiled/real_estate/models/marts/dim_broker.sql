
WITH broker_data AS (
    SELECT DISTINCT broker_name, broker_rank, update_date
    FROM "dev"."public"."staging_table"
), broker_table AS (
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY broker_name, update_date ORDER BY broker_name, broker_rank) AS rn,
        broker_name,
        broker_rank,
        update_date
    FROM broker_data
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY broker_name, broker_rank) as broker_id,
    update_date,
    broker_name,
    broker_rank
FROM broker_table
WHERE rn = 1