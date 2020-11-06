# Project Overview

A music streaming startup, Sparkify would like to move their process to cloud services. The data resided in S3 as a JSON file and should be transfered in Amazon Redshift using ETL pipeline. This will help analytics team to collaborate better and continue finding insights in the user activity.

# Setup Instructions:

## 1. Create an Amazon Web Services Account:
https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em_127222

## 2. Create an Identity and Access Management(IAM) User and Define Role:
- Create the user: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html
- Define the role as `AdministratorAccess`
- Copy the access key and secret in dwh.cfg file. Example below

```
[AWS]
KEY= YOUR_AWS_KEY
SECRET= YOUR_AWS_SECRET
```
## 3. Create a redshift cluster:
- Use the setting below to create the cluster in `infrastructure-as-code` (Lesson 3/Exercise 2).
- Once the cluster is ready, use the link address as host: `<your-cluster-idenfitier>.<some-domain>.<region>.redshift.amazonaws.com`
```
DWH_CLUSTER_TYPE=<single or multi node cluster>
DWH_NUM_NODES=<number of nodes>
DWH_NODE_TYPE=<Node type e.g. dc2.large>
DWH_CLUSTER_IDENTIFIER=<cluster identifier>
DWH_DB=<db name>
DWH_DB_USER=<db user>
DWH_DB_PASSWORD=<db password>
DWH_PORT=<db port. default - 5439>
```

## 4. Populate dwh.cfg file:

```
[CLUSTER]
HOST=<host address in step 3>
DB_NAME=<db name>
DB_USER=<db user>
DB_PASSWORD=<db password>
DB_PORT=5439

[IAM_ROLE]
ARN=<step 2 - YOUR_AWS_KEY>

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'
```
## 5. Run The Python Scripts:
- Run create_tables.py to drop and create tables
- Run etl.py to complete the transfer

# Dataset used

* **Song data**: ```s3://udacity-dend/song_data```
* **Log data**: ```s3://udacity-dend/log_data```
