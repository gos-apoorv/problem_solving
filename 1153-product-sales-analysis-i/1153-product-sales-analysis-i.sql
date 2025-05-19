# Write your MySQL query statement below
Select P.product_name,S.year, S.price 
From Sales S 
Left join Product P on S.product_id=P.product_id