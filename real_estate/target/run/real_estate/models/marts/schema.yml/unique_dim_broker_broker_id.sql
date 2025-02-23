select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    broker_id as unique_field,
    count(*) as n_records

from "dev"."public"."dim_broker"
where broker_id is not null
group by broker_id
having count(*) > 1



      
    ) dbt_internal_test