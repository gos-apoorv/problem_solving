# Write your MySQL query statement below
With tmp as(
Select
machine_id, process_id, max(timestamp) - min(timestamp) as diff
from Activity
Group by 1, 2
)
Select machine_id,
round(avg(diff), 3) processing_time
from tmp
Group by 1