from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator


# kubernator operator instead of docker operator

default_args = {
    "owner": "paul",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 27),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "hln_scraper",
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    # task_1 = DockerOperator(
    #     task_id="hln_scraper",
    #     image="paulstrazzulla/hln_scraper:latest",
    task_1 = BashOperator(
        task_id="hln_scraper",
        bash_command="ls",
    )
    task_1
