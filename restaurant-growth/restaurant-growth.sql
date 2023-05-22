# Write your MySQL query statement below
with temp as
(
    select 
        visited_on
        , sum(amount)
        as amount
    from Customer
    group by visited_on

),
temp1 as
(select visited_on
        , sum(amount)  over (order by visited_on
            rows between 6 preceding and current row)
            as amount
    from temp
    order by visited_on
    limit 6, 18446744073709551615)

select 
    visited_on
    , amount
    , round(amount/7, 2) as average_amount
    from temp1
    order by visited_on