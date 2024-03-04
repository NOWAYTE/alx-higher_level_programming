-- a script that lists all genres and displayss the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
  FROM tv_genres
  INNER JOIN tv_show_genres