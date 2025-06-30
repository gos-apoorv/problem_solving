-- Write your PostgreSQL query statement below

With tmp as (
    Select count(product_key) as total_products
    from Product 
)
Select c.customer_id 
From Customer c
Cross Join tmp
Group by 1
Having count(distinct c.product_key) = min(tmp.total_products)
