from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("dag", 
        start_date=datetime(2023,10,10), 
        schedule_interval="@daily", catchup=False) as dag:
        