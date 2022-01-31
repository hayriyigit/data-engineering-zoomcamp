import os
from datetime import datetime
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from ingest_script import ingest_callable

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

PG_HOST = os.getenv('PG_HOST')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE = os.getenv('PG_DATABASE')

URL_PREFIX = 'https://s3.amazonaws.com/nyc-tlc/trip+data'
URL = URL_PREFIX + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
OUTPUT_FILENAME = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
TABLE_NAME = 'yellow_taxi_{{ execution_date.strftime(\'%Y_%m\') }}'

local_workflow = DAG(
    "LocalIngestionDag",
    schedule_interval = "0 6 2 * *",
    start_date = datetime(2021, 1, 1)
)

with local_workflow:
    wget_task = BashOperator(
        task_id = 'wget',
        bash_command = f'curl -sSL {URL} > {OUTPUT_FILENAME}'
    )

    ingest_task = PythonOperator(
        task_id = 'ingest',
        python_callable = ingest_callable,
        op_kwargs = dict(
            host = PG_HOST,
            user = PG_USER,
            password = PG_PASSWORD,
            port = PG_PORT,
            db = PG_DATABASE,
            table_name = TABLE_NAME,
            csv_file = OUTPUT_FILENAME
        )
    )

    wget_task >> ingest_task