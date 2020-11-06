import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['KEYS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['KEYS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    """
    Description:
        Create a spark session as hadoop
    :return: A spark instance
    """
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Description:
        Load the data provided, process song and artist dimension tables
    :param spark: spark session
    :param input_data: input file location
    :param output_data: output file location
    """

    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data/*/*/*/*.json")

    # read song data file
    df = spark.read.json(song_data)

    # create a view for spark sql
    df.createOrReplaceTempView("songs")

    # extract columns to create songs table
    songs_table = spark.sql("""
                        SELECT DISTINCT song_id, title, artist_id, artist_name, year, duration
                        FROM songs
                        WHERE song_id IS NOT NULL                         
                    """)

    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy('year', 'artist_id').parquet(os.path.join(output_data, 'songs.parquet'), 'overwrite')

    # extract columns to create artists table
    artists_table = spark.sql("""
                            SELECT DISTINCT artist_id, name, location, latitude, longitude
                            FROM songs
                            WHERE artist_id IS NOT NULL
                        """)

    # write artists table to parquet files
    artists_table.write.parquet(output_data + 'artists_table/')


def process_log_data(spark, input_data, output_data):
    """
    DESCRIPTION:
        Load log files and tables from S3, process data into output tables and write tables to s3

    :param spark: spark session
    :param input_data: s3 bucket input file path
    :param output_data: s3 bucket output file path
    :return: NONE
    """
    # get filepath to log data file
    log_data = os.path.join(input_data, 'log_data/*.json')

    # read log data file
    df = spark.read.json(log_data_path)

    # filter by actions for song plays
    df = log_df.filter(log_df.page == 'NextSong')

    # create a view for spark sql
    df.createOrReplaceTempView("log_table")

    # extract columns for users table
    user_table = spark.sql("""
                        SELECT DISTINCT userId, firstName, lastName, gender, level
                        FROM log_table
                        WHERE userId IS NOT NULL
                        """)

    # write users table to parquet files
    user_table.write.parquet(output_data + 'user_table/')

    # extract columns to create time table
    time_table = spark.sql(""" 
                        SELECT  time_table.starttime as start_time, 
                                hour(time_table.starttime) as hour, 
                                dayofmonth(time_table.starttime) as day, 
                                weekofyear(time_table.starttime) as week, 
                                month(time_table.starttime) as month, 
                                year(time_table.starttime) as year, 
                                dayofweek(time_table.starttime) as weekday 
                        FROM (
                                SELECT to_timestamp(log_table.ts/1000) as starttime 
                                FROM log_table
                                WHERE log_table.ts IS NOT NULL ) as time_table 
                            """)

    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year", "month").parquet(output_data + 'time_table/')

    # read in song data to use for songplays table
    song_df = spark.read.parquet(output_data + 'songs_table/')

    # extract columns from joined song and log datasets to create songplays table
    songplays_table = spark.sql("""
                                SELECT  monotonically_increasing_id() as songplay_id,
                                        l.userId as user_id,
                                        l.level as level,
                                        s.song_id as song_id,
                                        s.artist_id as artist_id,
                                        l.sessionId as session_id,
                                        l.location as location,
                                        l.userAgent as user_agent,
                                        to_timestamp(l.ts/1000) as start_time,
                                        month(to_timestamp(l.ts/1000) as month,
                                        year(to_timestamp(l.ts/1000)) as year,
                                FROM log_table as l
                                    INNER JOIN songs as s 
                                        ON (l.artist = s.artist_name AND l.song = s.title)
    """)

    # write songplays table to parquet files partitioned by year and month
    songplays_tablesongplays_table.write.partitionBy("year", "month").parquet(output_data + 'songplays_table/')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://spark-project-bucket/"

    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
