# Write your MySQL query statement below

# update Users
# set name = upper(left(name, 1)) + lower(right(name, length(name)-1));

Select user_id,
      CONCAT(UPPER(LEFT(name, 1)),
        LOWER(RIGHT(name, LENGTH(name) - 1))) as name from Users order by user_id;