-- a script that lists all shows contained in hbtn_0d_tvshow
SELECT tv_shows.title, tv_shows_genres.genre_id
    FROM tv_shows_genres
    INNER JOIN tv_shows
    ON tv_shows.id = tv_shows_genres.show id
    ORDER BY tv_shows.title, tv_shows_genres.genre_id;