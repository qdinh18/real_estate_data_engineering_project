
    
    

with child as (
    select post_id as from_field
    from "re"."public"."fact_all_apartment"
    where post_id is not null
),

parent as (
    select post_id as to_field
    from "re"."public"."dim_post"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


