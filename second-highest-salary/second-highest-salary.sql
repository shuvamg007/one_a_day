# Write your MySQL query statement below
with temp as (select salary, dense_rank() over (order by salary desc) as ranking from Employee)
select ifnull((select salary from temp where ranking = 2 limit 1), null) as SecondHighestSalary;