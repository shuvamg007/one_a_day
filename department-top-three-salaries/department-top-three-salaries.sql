# Write your MySQL query statement below
WITH sales_table AS (
    SELECT
        id
        , DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as ranking
    FROM Employee
), relevant_ids AS (
    SELECT * FROM sales_table
    WHERE ranking <= 3
)
SELECT 
    t2.name AS Employee
    , t2.salary as Salary
    , t3.name as Department
FROM relevant_ids AS t1
LEFT JOIN Employee AS t2 on t1.id = t2.id
LEFT JOIN Department as t3 on t2.departmentId = t3.id;