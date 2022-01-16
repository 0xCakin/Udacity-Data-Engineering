# Data Engineering Nanodegree Program

This nanodegree program is designed to learn data model architecture, data lakes and warehouses, data pipeline automation and working with massive datasets.

SQL and Python programming skills are used to build the project solutions.

Nanodegree program details: [Udacity's Data Engineering Nanodegree](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

----


[Project 1 - Data Modeling with Postgres](https://github.com/canerakin111/Udacity-Data-Engineering/tree/master/1_Data_Modeling_with_Postgres)

The purpose of the project is understanding what songs users are listening and analyzing the data based on songs and user activity on the app.

[Project 2 - Data Modeling with Apache Cassandra](https://github.com/canerakin111/Udacity-Data-Engineering/tree/master/2_Data_Modeling_with_Apache_Cassandra)

In this project, ETL pipeline has been created to read the given csv file and implemented into Apache Cassandra. This task has been completed with the steps below.

- Merge all provided csv files into one file
- Design the queries to be implemented
- Create the tables based on the queries

[Project 3 - Data Warehouse](https://github.com/canerakin111/Udacity-Data-Engineering/tree/master/3_Data_Warehouse)	

A music streaming startup, Sparkify would like to move their process to cloud services. The data resided in S3 as a JSON file and should be transfered in Amazon Redshift using ETL pipeline. This will help analytics team to collaborate better and continue finding insights in the user activity.

[Project 4 - ETL Pipeline](https://github.com/canerakin111/Udacity-Data-Engineering/tree/master/5_Airflow_data_pipelines)

In this project, data has been extracted from a AWS S3 bucket. The data processed, fact and dimension tables have been created. The final output has been load back into S3. This process has been deployed in Spark session.


[Project 5 - Airflow Data Pipelines](https://github.com/canerakin111/Udacity-Data-Engineering/blob/master/5_Airflow_data_pipelines)

In this project, ETL pipeline is built on cloud using AWS Redshift and populated via Apache Airflow. The star-schema was used for dimensional model. The data consists of listening event logs from a music app Sparkify and data about songs, artists, and users.
The process looks like the following:
1. Stage the logs from S3 to staging tables in Redshift using a custom Airflow Operator
2. Move data from staging tables to our star schema tables using PostgresOperator
3. Check Data quality on the tables using custom Airflow operator


[Project 6 - Capstone Project](https://github.com/canerakin111/Udacity-Data-Engineering/tree/master/6_CapstoneProject)

This project aims to analyze immigration events using I94 Immigration data and city temperature data. Joining these two datasets will provide us a wider range of motion to complete this task.

![Nanodegree](https://github.com/canerakin111/Udacity_Predictive_Analysis/blob/master/Nanodegree_predictive_analytics.jpg)
