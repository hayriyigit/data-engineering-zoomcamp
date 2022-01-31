# Data Engineering Zoomcamp

### [Week 1: Introduction & Prerequisites](https://github.com/hayriyigit/data-engineering-zoomcamp/tree/main/Week-1)

-  [x] Introduction to GCP
-  [x]  Docker and docker-compose
-  [x]  Running Postgres locally with Docker
-  [x]  Setting up infrastructure on GCP with Terraform
-  [x]  Preparing the environment for the course
-  [x]  Homework


### [Week 2: Data ingestion](week_2_data_ingestion)
Goal: Orchestrating a job to ingest web data to a Data Lake in its raw form.
   
-  Data Lake (GCS)
    -  [x] Basics, What is a Data Lake
    -  [x] ELT vs. ETL
    -   Alternatives to components (S3/HDFS, Redshift, Snowflake etc.)
-  Orchestration (Airflow) 
    -   Basics
        -   [x] What is an Orchestration Pipeline?
        -   [x] What is a DAG?


### [Week 3: Data Warehouse](#)

Goal: Structuring data into a Data Warehouse

-   Data warehouse (BigQuery) 
    -   What is a data warehouse solution
    -   What is big query, why is it so fast, Cost of BQ,
    -   Partitoning and clustering, Automatic re-clustering 
    -   Pointing to a location in google storage 
    -   Loading data to big query & PG (10 min) -- using Airflow operator?
    -   BQ best practices
    -   Misc: BQ Geo location, BQ ML
    -   Alternatives (Snowflake/Redshift)

### [Week 4: Analytics engineering](#)

Goal: Transforming Data in DWH to Analytical Views

* Basics 
    * What is DBT?
    * ETL vs ELT 
    * Data modeling
    * DBT fit of the tool in the tech stack
* Usage (Combination of coding + theory) 
    * Anatomy of a dbt model: written code vs compiled Sources
    * Materialisations: table, view, incremental, ephemeral  
    * Seeds 
    * Sources and ref  
    * Jinja and Macros 
    * Tests  
    * Documentation 
    * Packages 
    * Deployment: local development vs production 
    * DBT cloud: scheduler, sources and data catalog (Airflow)
* Google data studio -> Dashboard
* Extra knowledge:
    * DBT cli (local)



### [Week 5: Batch processing](#)

Goal: 


* Distributed processing (Spark) 
    * What is Spark, spark cluster 
    * Explaining potential of Spark
    * What is broadcast variables, partitioning, shuffle
    * Pre-joining data
    * use-case
    * What else is out there (Flink)
* Extending Orchestration env (airflow)
    * Big query on airflow 
    * Spark on airflow 


### [Week 6: Streaming](#)

Goal: 

* Basics
    * What is Kafka
    * Internals of Kafka, broker
    * Partitoning of Kafka topic
    * Replication of Kafka topic
* Consumer-producer
* Schemas (avro)
* Streaming
    * Kafka streams
* Kafka connect
* Alternatives (PubSub/Pulsar)


### [Week 7, 8 & 9: Project](#)

* Putting everything we learned to practice

Duration: 2-3 weeks

* Upcoming buzzwords
  *  Delta Lake/Lakehouse
    * Databricks
    * Apache iceberg
    * Apache hudi
  * Data mesh
  * KSQLDB
  * Streaming analytics
  * Mlops

