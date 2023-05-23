# Write your MySQL query statement below
with temp1 as (
    select Users.name as results
    from Users
    inner join MovieRating
    on Users.user_id = MovieRating.user_id
    group by Users.user_id
    order by count(*) desc, results asc
    limit 1
), temp2 as (
    select Movies.title as results
    from Movies
    inner join MovieRating
    on Movies.movie_id = MovieRating.movie_id
    where YEAR(MovieRating.created_at) = "2020" and MONTH(MovieRating.created_at) = '2'
    group by Movies.movie_id
    order by avg(MovieRating.rating) desc, results asc
    limit 1
)
select * from temp1
union all
select * from temp2


