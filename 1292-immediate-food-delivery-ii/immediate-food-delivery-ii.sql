-- Write your PostgreSQL query statement below
With first_order as (
    Select
    customer_id,
    order_date,
    customer_pref_delivery_date,
    rank() over ( partition by customer_id order by order_date asc ) as order_rank
    From Delivery 
)
Select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end ) * 100.00 / count(customer_id),2) as immediate_percentage
from first_order
where order_rank = 1