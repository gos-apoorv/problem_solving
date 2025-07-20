-- Write your PostgreSQL query statement below
With t as (
    Select 'failed' as period_state,
    fail_date as period_date
    From Failed
    union all
    Select 'succeeded' as period_state,
    success_date as period_date
    From Succeeded
),
t2 as (
    Select period_state, 
    period_date,
    row_number() over (partition by period_state order by period_date) as rn
    From t 
    Where period_date between '2019-01-01' and '2019-12-31'
    Order by 2 asc
)
Select period_state,
min(period_date) as start_date,
max(period_date) as end_date
from t2
Group by (period_date - INTERVAL '1 day' * rn, 1)
Order by 2,1