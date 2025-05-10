# Write your MySQL query statement below
Select 
i.unique_id,
e.name
From Employees e
Left join EmployeeUNI i on e.id = i.id
