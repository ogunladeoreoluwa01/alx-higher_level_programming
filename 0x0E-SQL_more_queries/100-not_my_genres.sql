-- This shows all the shows in the hbtn_0d_tvshows which have
-- Those without a genre are represented by NULL
SELECT name FROM tv_genres
WHERE id NOT IN (
	SELECT genre_id FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE title = 'Dexter'
)
ORDER BY name ASC;
