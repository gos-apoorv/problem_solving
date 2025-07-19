
Select
distinct l.page_id as recommended_page
From Friendship f
Join Likes l on f.user1_id = l.user_id or f.user2_id = l.user_id 
where 1=1
and (user1_id = 1 or user2_id = 1)
and user1_id != user2_id
and l.page_id not in 
(Select page_id from Likes where user_id = 1)