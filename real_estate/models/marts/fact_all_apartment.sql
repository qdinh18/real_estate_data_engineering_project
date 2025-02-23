{{ config(materialized='table') }}
WITH staging_data AS (
SELECT ROW_NUMBER() OVER (PARTITION BY s.update_date, s.url ORDER BY s.update_date) AS rn,
	   dpo.post_id,
       s.update_date,
       db.broker_id,
       dp.project_id,
       s.price,
       'tỷ đồng'::TEXT AS price_unit,
       s.price_per_m²,
       'triệu đồng'::TEXT AS price_per_m²_unit,
       s.area,
       'm²'::TEXT AS area_unit,
       s.bedroom,
       s.bathroom
FROM {{ ref('staging_table') }} s   
                    LEFT JOIN {{ ref('dim_broker') }} db ON s.broker_name = db.broker_name
											 AND s.broker_rank = db.broker_rank
                                            AND s.update_date::date = db.update_date::date
                    LEFT JOIN {{ ref('dim_project') }} dp ON s.project_name = dp.project_name 
                                            AND s.update_date::date = dp.update_date::date
                    LEFT JOIN {{ ref('dim_post') }} dpo ON s.title = dpo.title 
                                            AND s.url = dpo.url 
                                            AND s.update_date::date = dpo.update_date::date
ORDER BY dpo.post_id
) SELECT post_id,
       update_date,
       broker_id,
       project_id,
       price,
       price_unit,
       price_per_m²,
       price_per_m²_unit,
       area,
       area_unit,
       bedroom,
       bathroom 
FROM staging_data 
WHERE rn = 1