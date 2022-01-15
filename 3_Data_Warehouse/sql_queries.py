import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
                        CREATE TABLE IF NOT EXISTS staging_events
                        (
                            artist          VARCHAR,
                            auth            VARCHAR, 
                            firstName       VARCHAR,
                            gender          VARCHAR,   
                            itemInSession   INTEGER,
                            lastName        VARCHAR,
                            length          FLOAT,
                            level           VARCHAR, 
                            location        VARCHAR,
                            method          VARCHAR,
                            page            VARCHAR,
                            registration    BIGINT,
                            sessionId       INTEGER,
                            song            VARCHAR,
                            status          INTEGER,
                            ts              TIMESTAMP,
                            userAgent       VARCHAR,
                            userId          INTEGER
                        ); """)

staging_songs_table_create = ("""
                        CREATE TABLE IF NOT EXISTS staging_songs
                        (
                            song_id            VARCHAR,
                            num_songs          INTEGER,
                            title              VARCHAR,
                            artist_name        VARCHAR,
                            artist_latitude    FLOAT,
                            year               INTEGER,
                            duration           FLOAT,
                            artist_id          VARCHAR,
                            artist_longitude   FLOAT,
                            artist_location    VARCHAR
                        ); """)
songplay_table_create = ("""
                        CREATE TABLE IF NOT EXISTS fact_songplay
                        (
                            songplay_id          INTEGER IDENTITY(0,1) PRIMARY KEY sortkey,
                            start_time           TIMESTAMP,
                            user_id              INTEGER,
                            level                VARCHAR,
                            song_id              VARCHAR,
                            artist_id            VARCHAR,
                            session_id           INTEGER,
                            location             VARCHAR,
                            user_agent           VARCHAR
                        ); """)

user_table_create = ("""
                        CREATE TABLE IF NOT EXISTS dim_user
                        (
                            user_id INTEGER PRIMARY KEY distkey,
                            first_name      VARCHAR,
                            last_name       VARCHAR,
                            gender          VARCHAR,
                            level           VARCHAR
                        ); """)

song_table_create = ("""
                        CREATE TABLE IF NOT EXISTS dim_song
                        (
                            song_id     VARCHAR PRIMARY KEY,
                            title       VARCHAR,
                            artist_id   VARCHAR distkey,
                            year        INTEGER,
                            duration    FLOAT
                        ); """)

artist_table_create = ("""
                        CREATE TABLE IF NOT EXISTS dim_artist
                        (
                            artist_id          VARCHAR PRIMARY KEY distkey,
                            name               VARCHAR,
                            location           VARCHAR,
                            latitude           FLOAT,
                            longitude          FLOAT
                        ); """)

time_table_create = ("""
                        CREATE TABLE IF NOT EXISTS dim_time
                        (
                            start_time    TIMESTAMP PRIMARY KEY sortkey distkey,
                            hour          INTEGER,
                            day           INTEGER,
                            week          INTEGER,
                            month         INTEGER,
                            year          INTEGER,
                            weekday       INTEGER
                        ); """)


# STAGING TABLES

staging_events_copy = ("""
                        COPY staging_events
                        FROM {}
                        iam_role {}
                        FORMAT AS json {};
                        """).format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
                        COPY staging_songs
                        FROM {}
                        iam_role {}
                        FORMAT AS json 'auto';
                        """).format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES

songplay_table_insert = ("""
                        INSERT INTO fact_songplay(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                        SELECT DISTINCT to_timestamp(to_char(se.ts, '9999-99-99 99:99:99'),'YYYY-MM-DD HH24:MI:SS'),
                                        se.userId,
                                        se.level,
                                        ss.song_id,
                                        ss.artist_id,
                                        se.sessionId,
                                        se.location,
                                        se.userAgent
                        FROM staging_events se
                            JOIN staging_songs ss ON (se.song = ss.title AND se.artist = ss.artist_name) AND se.page = 'NextSong';
                        """)

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
                        SELECT DISTINCT user_id, 
                                        first_name, 
                                        last_name, 
                                        gender, 
                                        level
                        FROM staging_events
                        WHERE page = 'NextSong' AND user_id IS NOT NULL;
                        """)

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
                        SELECT DISTINCT song_id, 
                                        title, 
                                        artist_id, 
                                        year, 
                                        duration
                        FROM staging_songs
                        WHERE song_id IS NOT NULL;
                        """)
artist_table_insert = ("""INSERT INTO artist(artist_id, name, location, latitude, longitude)
                          SELECT DISTINCT artist_id, 
                                          artist_name, 
                                          artist_location, 
                                          artist_latitude, 
                                          artist_longitude 
                          FROM staging_songs
                          WHERE artist_id IS NOT NULL;
                          """)

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekDay)
                        SELECT start_time, 
                               extract(hour from start_time), 
                               extract(day from start_time),
                               extract(week from start_time), 
                               extract(month from start_time),
                               extract(year from start_time), 
                               extract(dayofweek from start_time)
                        FROM songplay""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
