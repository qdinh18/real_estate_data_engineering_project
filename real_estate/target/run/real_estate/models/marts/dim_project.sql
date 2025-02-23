
  
    

  create  table
    "dev"."public"."dim_project__dbt_tmp"
    
    
    
  as (
    
WITH project_data AS (
    SELECT DISTINCT project_name,
                    investor, 
                    project_area_range, 
                    project_status, 
                    address, 
                    number_of_apartments, 
                    number_of_buildings,
                    update_date
    FROM "dev"."public"."staging_table"
), project_table AS (
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY project_name, update_date ORDER BY project_name, address) AS rn,
        project_name,
        investor, 
        project_area_range, 
        project_status, 
        address, 
        number_of_apartments, 
        number_of_buildings,
        update_date
    FROM project_data
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY project_name, 
                                investor, 
                                project_area_range, 
                                project_status, 
                                address, 
                                number_of_apartments, 
                                number_of_buildings
    ) as project_id,
    update_date,
    project_name, 
    investor, 
    project_area_range, 
    project_status, 
    address, 
    number_of_apartments, 
    number_of_buildings
FROM project_table
WHERE rn = 1
  );
  