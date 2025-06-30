-- Write your PostgreSQL query statement below

With tmp as (
    Select count(distinct product_key) as total_products
    from Product 
)
Select c.customer_id 
From Customer c
Join Product p on c.product_key = p.product_key
Cross Join tmp
Group by 1
Having count(distinct p.product_key) = min(tmp.total_products)
