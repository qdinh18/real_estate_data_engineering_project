select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select broker_name
from "dev"."public"."dim_broker"
where broker_name is null



      
    ) dbt_internal_test