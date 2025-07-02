# Write your MySQL query statement below

With tmp as 
(Select  count(distinct r.post_id) / count(distinct a.post_id) as daily_avg
From Actions a
Left Join Removals r on a.post_id=r.post_id
where a.extra='spam'
GRoup by a.action_date)
Select round(avg(daily_avg), 4) * 100 as average_daily_percent
From tmp

