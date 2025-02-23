select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    project_id as unique_field,
    count(*) as n_records

from "dev"."public"."dim_project"
where project_id is not null
group by project_id
having count(*) > 1



      
    ) dbt_internal_test