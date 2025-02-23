select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select url
from "dev"."public"."dim_post"
where url is null



      
    ) dbt_internal_test