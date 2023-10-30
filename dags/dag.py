from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

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
    task_1 = KubernetesPodOperator(
        name="hln_scraper",
        image="paulstrazzulla/hln_scraper:latest",
        image_pull_policy="always",
        labels={"pipeline": "test_docker_pipeline"},
        task_id='task___test-run-hln_scraper',

    )
    task_1

