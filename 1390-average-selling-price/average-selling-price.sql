-- Write your PostgreSQL query statement below
Select
p.product_id,
coalesce(round(sum(p.price * u.units)*1.00/sum(u.units),2), 0) as average_price
From Prices p 
left join UnitsSold u on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
Group By 1