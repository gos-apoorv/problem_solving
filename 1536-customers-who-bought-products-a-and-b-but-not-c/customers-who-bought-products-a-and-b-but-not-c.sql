-- Write your PostgreSQL query statement below
Select 
c.customer_id, c.customer_name
From Customers c 
Join Orders o on c.customer_id = o.customer_id
Group by 1,2
Having 1=1
and sum(case when o.product_name = 'A' then 1 else 0 end) >= 1
and sum(case when o.product_name = 'B' then 1 else 0 end) >= 1
and sum(case when o.product_name = 'C' then 1 else 0 end) < 1
Order by 1
