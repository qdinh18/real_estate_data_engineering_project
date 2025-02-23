
    
    

with child as (
    select project_id as from_field
    from "re"."public"."fact_all_apartment"
    where project_id is not null
),

parent as (
    select project_id as to_field
    from "re"."public"."dim_project"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


