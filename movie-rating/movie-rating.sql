# Write your MySQL query statement below
(
    select Users.name as results
    from Users
    inner join MovieRating
    on Users.user_id = MovieRating.user_id
    group by Users.user_id
    order by count(*) desc, results asc
    limit 1
)
UNION ALL
(
    select Movies.title as results
    from Movies
    inner join MovieRating
    on Movies.movie_id = MovieRating.movie_id
    where MovieRating.created_at like "2020-02%"
    group by Movies.movie_id
    order by avg(MovieRating.rating) desc, results asc
    limit 1
)


