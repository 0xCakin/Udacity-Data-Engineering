# PROJECT 1 - Data Modeling with Postgres

**This project has been created for the new startup called Sparkify.**

The purpose of the project is understanding what songs users are listening and analyzing the data based on songs and user activity on the app.

**Milestones of this project:**
- Build an ETL pipeline using Python
    - Define fact and dimension tables for a star schema
    - Create an ETL pipeline to transfer data from files to tables
    
# Database Tables:
- songs: fact data of the songs in the app
- artists: fact data of the artists in the app
- users: fact data of the app users
- time: timestamp of user activity data
- songplays: user listening activity data


# Procedure:

## Set up:
1. Install postgres and psycopg2-binary
2. Point postgres to the host port number and host name

## Process:
1. Run create_tables.py to create the schema.
    1. This will run sql_queries.py script to create & drop tables.
2. Run etl.py to create to populate the tables.
    1. This will populate the tables with sql_queries.py


# Files in this Repo:
- Data
    - log_data
    - song_data
- README.md
- create_tables.py
- etl.ipynb
- etl.py
- sql_queries.py
- test.ipynb

 EX Query:
``` sql
    SELECT Count(*) agent_count, user_agent FROM SongPlays
    GROUP BY user_agent
    
```
