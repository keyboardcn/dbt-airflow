from datetime import timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

from task1 import load_seed_task

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'retries': 0,
    'retry_delay':timedelta(seconds=30),
}


dag = DAG(
        dag_id='airflow_dbt_scheduler',
        default_args=default_args,
        schedule_interval=timedelta(minutes=5),
    )


def data_transform_task(dag_dummy: DAG) -> BashOperator:
    return BashOperator(
        task_id='daily_transform',
        bash_command= 'cd /tmp && echo "hello2" >> task.txt && echo hello task 2',
        # bash_command='cd /dbt && dbt run --models transform --profiles-dir .',
        env={
            # Commented out as we not use
            # 'dbt_user': '{{ var.value.dbt_user }}',
            # 'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag_dummy
    )

task_1 = load_seed_task(dag_dummy=dag)
task_2 = data_transform_task(dag_dummy=dag)
task_1 >> task_2 # Define dependencies