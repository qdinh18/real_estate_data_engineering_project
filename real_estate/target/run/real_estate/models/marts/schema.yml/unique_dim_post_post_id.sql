select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    post_id as unique_field,
    count(*) as n_records

from "dev"."public"."dim_post"
where post_id is not null
group by post_id
having count(*) > 1



      
    ) dbt_internal_test