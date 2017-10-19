-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column - RIGHT JOIN
-- Each record should display: tv_shows.title - tv_genres.name - SELECT
-- Results must be sorted in ascending order by the show title and genre name - ORDER BY

SELECT shows.title, genres.name
	FROM tv_genres AS genres JOIN tv_show_genres AS ids RIGHT JOIN tv_shows AS shows
	ON genres.id = ids.genre_id AND ids.show_id = shows.id
	ORDER BY shows.title, genres.name ASC;
