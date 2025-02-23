select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select post_id
from "dev"."public"."dim_post"
where post_id is null



      
    ) dbt_internal_test