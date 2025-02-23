select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select broker_id
from "dev"."public"."fact_all_apartment"
where broker_id is null



      
    ) dbt_internal_test