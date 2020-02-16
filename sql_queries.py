# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id BIGSERIAL PRIMARY KEY,
        start_time TIMESTAMP,
        user_id INT,
        level TEXT NOT NULL,
        song_id TEXT,
        artist_id TEXT,
        session_id INT NOT NULL,
        location TEXT NOT NULL,
        user_agen TEXT NOT NULL
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY, 
        first_name TEXT NOT NULL, 
        last_name TEXT NOT NULL, 
        gender TEXT NOT NULL, 
        level TEXT NOT NULL
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id TEXT PRIMARY KEY, 
        title TEXT NOT NULL, 
        artist_id TEXT, 
        year INT NOT NULL, 
        duration NUMERIC
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id TEXT PRIMARY KEY, 
        name TEXT NOT NULL, 
        location TEXT NOT NULL, 
        latitude NUMERIC, 
        longitude NUMERIC
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY, 
        hour INT, 
        day INT, 
        week INT, 
        month INT, 
        year INT, 
        weekday TEXT
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays 
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agen) VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users 
    (user_id, first_name, last_name, gender, level) VALUES 
    (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs
    (song_id, title, artist_id, year, duration) VALUES 
    (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists 
    (artist_id, name, location, latitude, longitude) VALUES 
    (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id 
    FROM songs 
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s 
    AND artists.name = %s 
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [time_table_create, artist_table_create, song_table_create, user_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]