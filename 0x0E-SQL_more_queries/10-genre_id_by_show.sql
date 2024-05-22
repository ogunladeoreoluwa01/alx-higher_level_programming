-- This shows all the shows in the hbtn_0d_tvshows which have
-- at least one show linked
SELECT title, genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
