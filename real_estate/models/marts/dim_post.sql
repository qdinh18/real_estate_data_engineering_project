{{ config(materialized='table') }}
WITH post_data AS (
    SELECT DISTINCT title,
                    url, 
                    posted_date, 
                    expired_date,
                    update_date
    FROM {{ ref('staging_table') }}
), post_table AS (
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY url, update_date ORDER BY title, url) AS rn,
        title,
        url, 
        posted_date, 
        expired_date,
        update_date
    FROM post_data
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY title, 
                                url, 
                                posted_date, 
                                expired_date
    ) as post_id,
    update_date,
    title, 
    url, 
    posted_date, 
    expired_date
FROM post_table
WHERE rn = 1