-- Write your PostgreSQL query statement below
Select
s.student_id,
s.student_name,
sb.subject_name,
count(e.subject_name) as attended_exams
From Students s 
Cross Join Subjects sb
Left Join Examinations e on s.student_id = e.student_id and sb.subject_name = e.subject_name
Group By 1,2,3
Order By 1, 3