
    
    

with child as (
    select broker_id as from_field
    from "re"."public"."fact_all_apartment"
    where broker_id is not null
),

parent as (
    select broker_id as to_field
    from "re"."public"."dim_broker"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


