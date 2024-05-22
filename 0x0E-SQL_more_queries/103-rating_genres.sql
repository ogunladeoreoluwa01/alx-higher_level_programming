-- this shows the sum of the ratings
SELECT name, sum(rate) AS rating
FROM tv_genres
NATURAL JOIN tv_show_genres
NATURAL JOIN tv_show_ratings
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id  = tv_show_ratings.show_id
GROUP BY genre_id
ORDER BY rating DESC;
