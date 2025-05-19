# Write your MySQL query statement below
With calc as (
Select id, num , LEAD(num, 1, 0) over (order by id) as next_num
, LEAD(num, 2, -1) over (order by id) as next_2_num
From Logs
order by id
)
Select distinct num as ConsecutiveNums
from calc
where num = next_num
and next_num = next_2_num