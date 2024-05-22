-- This shows all the shows in the hbtn_0d_tvshows which have
-- Those without a genre are represented by NULL
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
