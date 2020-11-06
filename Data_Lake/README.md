# Sparkify Data Lake | ETL Pipeline

## Summary

 - [Introduction](#introduction)
 - [Getting started](#getting-started)
 - [Data sources](#data-sources)
 - [Parquet data schema](#parquet-data-schema)
## Project Overview
 In this project, data has been extracted from a AWS S3 bucket. The data processed, fact and dimension tables have been created. The final output has been load back into S3. This process has been deployed in Spark session.
## Pre-requisite 
1. Install [Python 3](https://www.python.org/)
2. Install pyspark, os, pyspark.sql
    `pip install pyspark`
    ##### _Optional:_
3. [Jupyter Notebook](https://jupyter.org/install)
4. [PyCharm](https://www.jetbrains.com/pycharm/download/)
  
## ETL Pipeline
1. Read data from S3
    - Song data: s3://udacity-dend/song_data
    - Log data: s3://udacity-dend/log_data
2. Transform the data using Spark
    - Create five different tables
    ### Fact Table
	 **songplays**  - data lives in log data.
    -   _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_

    ### Dimension Tables
	 **users**  - users
		Fields -   _user_id, first_name, last_name, gender, level_
		
	 **songs**  - songs in the database
    Fields - _song_id, title, artist_id, year, duration_
    
	**artists**  - artists in the database
    Fields -   _artist_id, name, location, lattitude, longitude_
    
	  **time**  - timestamps of records in  **songplays**  broken down into specific units
    Fields -   _start_time, hour, day, week, month, year, weekday_
## Setup Instructions:
1. Populate the dwh.cfg config file with AWSAccessKeyId and AWSSecretKey
2. Setup ETL.py and run 
```
[KEY]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
```
