(SELECT u.name as results
FROM MovieRating mr
JOIN Users u on mr.user_id =  u.user_id
GROUP BY 1
ORDER BY count(u.name) desc, u.name asc
limit 1)
UNION ALL
(SELECT m.title as results
FROM MovieRating mr
JOIN Movies m on mr.movie_id =  m.movie_id
where created_at >= '2020-02-01' and created_at < '2020-03-01'
GROUP BY 1
ORDER BY AVG(mr.rating) desc, m.title asc
limit 1)