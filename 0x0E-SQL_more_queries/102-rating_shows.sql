-- It shows each show and its ratings
SELECT title, sum(rate) AS rating
FROM tv_show_ratings
NATURAL JOIN tv_shows
WHERE tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_show_ratings.show_id
ORDER BY rating DESC;
