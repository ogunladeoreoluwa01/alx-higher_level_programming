-- This shows all shows and their genre
SELECT title, name FROM tv_shows
LEFT JOIN tv_show_genres
NATURAL JOIN tv_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id is NULL
OR tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
