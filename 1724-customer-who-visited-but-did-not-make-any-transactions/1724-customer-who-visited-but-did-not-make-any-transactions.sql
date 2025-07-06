# Write your MySQL query statement below

Select 
v.customer_id, 
count(distinct v.visit_id) as count_no_trans
From Visits v
Left Join Transactions t on v.visit_id = t.visit_id 
where t.transaction_id is null
Group by 1