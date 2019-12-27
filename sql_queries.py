# DROP TABLES
# These string variables are executed in drop_tables function in create_table.py

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# These string variables are executed in create_tables function in create_table.py

songplay_table_create = ("CREATE TABLE songplays(songplay_id int, start_time bigint NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar, PRIMARY KEY(songplay_id));")

user_table_create = ("CREATE TABLE users(user_id int, first_name varchar, last_name varchar, gender varchar, level varchar, PRIMARY KEY(user_id));")

song_table_create = ("CREATE TABLE songs(song_id varchar, tittle varchar, artist_id varchar, year int, duration float, PRIMARY KEY(song_id));")

artist_table_create = ("CREATE TABLE artists(artist_id varchar NOT NULL, name varchar, location varchar, latitude float, longitude float, PRIMARY KEY(artist_id));")

time_table_create = ("CREATE TABLE time(start_time bigint, hour int, day int, week int, month int, year int, weekday int, PRIMARY KEY(start_time));")


# INSERT RECORDS
# These string variables are executed in ETL process. They are used to insert records into tables

songplay_table_insert = ("INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

user_table_insert = ("INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level=EXCLUDED.level")

song_table_insert = ("INSERT INTO songs(song_id, tittle, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")


time_table_insert = ("INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")


# FIND SONGS
# It is used in ETL process. The purpose is to find song_id and artist_id values to insert to songplay data

song_select = ("""SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.tittle = (%s) AND artists.name = (%s) AND songs.duration = (%s)""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]