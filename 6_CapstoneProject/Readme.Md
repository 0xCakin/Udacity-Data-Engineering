# Temperature and US Immigration Data ETL Pipeline
### Data Engineering Capstone Project

#### Project Summary
This project aims to analyze immigration events using I94 Immigration data and city temperature data. Joining these two datasets will provide us a wider range of motion to complete this task.

## Data sources

### I94 Immigration Data
This data comes from the US National Tourism and Trade Office [here](https://travel.trade.gov/research/reports/i94/historical/2016.html).

### World Temperature Data
This dataset came from Kaggle [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).

### U.S. City Demographic Data
This data comes from OpenSoft [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).

## Data cleaning

* Filter temperature data to only use US data.
* Remove irregular ports from I94 data.
* Drop rows with missing IATA codes from I94 data. We need the IATA codes to join the data with other sources.

#### Conceptual Data Model 
Star schema is the simplest conceptual data model. It consists of one or multiple fact tables joining to numerous of dimension tables. In this project, Immigration data contains the major information. Therefore it is better to keep it as a fact table in this star schema and make foreign keys for other tables to connect immigration table. This will allow us to examine the data in a wider range. For example, we can connect temperature and immigration table to analyze the correlation between the temperature and immigration patterns. As another example, i94port table and immigration table join can determine immigration pattern to city and states.

Immigration Table:
- cicid     
- year     
- month    
- city     
- res      
- iport  
- arrdate  
- depdate  
- visa     
- addr 

The first dimension table is I94port. The columns are showed below.
- port_code --foreign key
- port_city 
- port_state 

The second dimension table will be the temperature data.
- AverageTemperature 
- City 
- Country 
- Latitude 
- Longitude 
- iport -- foreign key


#### Mapping Out Data Pipelines
As described in the step 2, data clean up should be completed first of all.
- Clean up and normalize the immigration data
- Clean up and normalize the temperature data
- Organize i94port data
- Run create_table.py file
- Join temperature data with i94port
- Insert the data into the database

### Choice of tools and technologies for the project
I used Panda library for this project which I am very comfortable with. It can easily handle multiple file formats (SAS, csv, etc) that contain large amounts of data. It is also easy to manipulate the data and very efficient. However it would be better to use Spark later to on to be able to utilize Amazon Web Services and Apache Airflow. Amazon Services will help (Redshift, EMR) to distribute the data very efficiently and Airflow will be useful for schedeling the process.

### How often the data should be updated
Since the format of the raw files are monthly, we should continue pulling the data monthly.
    
### FAQ
* When the data was increased by 100x, do you store the data in the same way? If your project is heavy on reading over writing, how do you store the data in a way to meet this requirement? What if the requirement is heavy on writing instead?
* * In that case, I would use Spark with EMR to process the data in a distributed way with high efficiency. In this project the data has been stored in Postgres database. However it can be better approach to use NoSQL database if the data gets much bigger. Apache Cassandra can be a great example since it is free and taught in Data Engineering course. Airflow can help to write the data into the database. It can scale above the 100 million rows.

* How do you run this pipeline on a daily basis by 7 am every day. What if the dag fails, how do you update the dashboard? Will the dashboard still work? Or will you populate the dashboard by using the last day?

* * I would use Airflow and create a DAG to monitor the process. If the dag fails, a trigger can be set up within Airflow to inform the Airflow operator or the data engineering team to troubleshoot the issue.

* How do you make your database could be accessed by 100+ people? Can you come up with a more cost-effective approach? Does your project need to support 100+ connections at the same time?

* * Redshift can be a good alternative if over 100+ people need to access the database. Redshift Great auto-scaling capabilities and can be accessed by many people. Amazon Web Services provides multiple options for Redshift. To make it cost-effective, we can choose the lowest node that is in our bugdet. PostgreSQL can be a cheaper option however the performance compared to redshift will be lower.