import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:password@localhost:5432/Hometask3')
con = engine.connect()

#1-ое задание
print(con.execute("""SELECT genre_name, COUNT(singer_id) AS Number from genresinger
JOIN genres ON genresinger.genre_id = genres.id
GROUP BY genre_name;""").fetchall())

#2-е задание
print(con.execute("""SELECT album_name, COUNT(track_name) AS "Quantity of tracks" FROM tracks AS t
JOIN albums ON t.album_id = albums.id
WHERE albums.release_date BETWEEN 2019 AND 2020
GROUP BY album_name;""").fetchall())

#3-e задание
print(con.execute("""SELECT album_name, ROUND(AVG(track_duration),2) AS "Average duration" FROM tracks AS t
JOIN albums ON t.album_id = albums.id
GROUP BY album_name;""").fetchall())

#4-e задание
print(con.execute("""SELECT singer_name, album_name FROM singers AS s
JOIN albumsinger ON s.id = albumsinger.singer_id
JOIN albums ON albumsinger.album_id = albums.id
WHERE albums.release_date != 2020;""").fetchall())

#5-e задание
print(con.execute("""SELECT collection_name FROM collection AS coll
JOIN collectiontracks AS ct ON coll.id = ct.collection_id
JOIN tracks AS t ON ct.track_id = t.id
JOIN albums AS a ON t.album_id = a.id
JOIN albumsinger AS asi ON a.id = asi.album_id
JOIN singers AS s ON asi.singer_id = s.id
WHERE singer_name LIKE '%%Eminem%%'
GROUP BY collection_name
;""").fetchall())

#6-e задание
print(con.execute("""SELECT album_name FROM albums AS al
JOIN albumsinger AS alsing ON al.id = alsing.album_id
JOIN singers AS s ON alsing.singer_id = s.id
JOIN genresinger AS gs ON s.id = gs.singer_id
JOIN genres AS g ON gs.genre_id = g.id
GROUP BY album_name
HAVING COUNT(genre_name) > 1
;""").fetchall())

#7-e задание
print(con.execute("""SELECT tracks.track_name FROM collectiontracks
RIGHT OUTER JOIN tracks ON collectiontracks.track_id = tracks.id
WHERE track_id is NULL
;""").fetchall())

#8-e задание
print(con.execute("""SELECT singer_name, track_duration FROM singers
JOIN albumsinger AS alsing ON singers.id = alsing.singer_id
JOIN albums AS al ON alsing.album_id = al.id
JOIN tracks ON al.id = tracks.album_id
WHERE track_duration = (SELECT MIN(tracks.track_duration) FROM tracks)
;""").fetchall())

#9-e задание
print(con.execute("""SELECT album_name FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP by album_name
HAVING COUNT(album_name) = (SELECT MIN(count) FROM
(SELECT album_name, COUNT(*) AS count FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP by album_name) AS al)
;""").fetchall())

