select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select update_date
from "dev"."public"."fact_all_apartment"
where update_date is null



      
    ) dbt_internal_test