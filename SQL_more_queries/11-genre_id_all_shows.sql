-- list all shows in hbtn_0d_tvshows
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, NULL)
from tv_shows
INNER JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.show_id;
