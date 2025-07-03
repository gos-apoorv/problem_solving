-- Write your PostgreSQL query statement below

Select
activity_date as day,
count(distinct user_id) as active_users
From Activity
where 1=1
and activity_date between date('2019-07-27') - INTERVAL '29 day' and date('2019-07-27')
group by 1