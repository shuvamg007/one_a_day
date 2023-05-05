# Write your MySQL query statement below

with temp1 as(select requester_id as id, count(*) as num from RequestAccepted
group by requester_id),
temp2 as (select accepter_id as id, count(*) as num from RequestAccepted
group by accepter_id),
temp3 as (select * from temp1 
union all
select * from temp2)
select id, sum(num) as num
from temp3 group by id
order by num desc
limit 1