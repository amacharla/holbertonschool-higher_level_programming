-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT genres.name
	FROM tv_genres AS genres JOIN tv_show_genres AS ids JOIN tv_shows AS shows
	ON genres.id = ids.genre_id AND ids.show_id = shows.id
	WHERE shows.title = 'Dexter'
	ORDER BY genres.name ASC;
