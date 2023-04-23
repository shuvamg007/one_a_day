# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE p FROM Person p, Person q where p.email = q.email and p.id > q.id;