-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT shows.title
	FROM tv_genres AS genres JOIN tv_show_genres AS ids JOIN tv_shows AS shows
	ON genres.id = ids.genre_id AND ids.show_id = shows.id
	WHERE genres.name = "Comedy"
	ORDER BY shows.title ASC;
