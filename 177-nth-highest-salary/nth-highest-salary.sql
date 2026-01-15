CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
    IF N < 1 THEN 
    RETURN;
    END IF;
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    Select max(a.salary) as Salary
    from (
        Select e.salary,
        dense_rank() over (order by e.salary desc) as rnk
        from Employee e
    ) a
    where rnk = N
      
  );
END;
$$ LANGUAGE plpgsql;