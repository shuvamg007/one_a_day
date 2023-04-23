# Write your MySQL query statement below
with temp as (SELECT product_id, SUM(unit) as unit FROM Orders where YEAR(order_date) = "2020" and MONTH(order_date) = "02" group by product_id)
select product_name, unit from temp 
left join Products on temp.product_id = Products.product_id
where temp.unit >= 100; 