-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: tv_genres.name - number of shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

SELECT tv_genres.name, COUNT(tv_show_genres.show_id) as "number_shows"
	FROM tv_genres, tv_show_genres
	WHERE tv_genres.id = tv_show_genres.genre_id
	GROUP BY tv_show_genres.genre_id
	ORDER by COUNT(tv_show_genres.show_id) DESC;
