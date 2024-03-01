-- a script that perfoms list allshows without a genre linked 
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_show_genres
  RIGHT JOIN tv_shows
  ON tv_show.id = tv_show_genres.show_id
  WHERE tv_show_genres.show_id IS NULL
  ORDER BY tv_shows.title, tv_show_genres.genre_id;