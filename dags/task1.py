from datetime import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator

from settings import start_date

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
    'retries': 0
}

with DAG('1_init_once_seed_data', default_args=default_args, schedule_interval='@once') as dag:
    task_1 = BashOperator(
        task_id='load_seed_data_once',
        bash_command= 'echo hello1 >> task.txt && echo hello task 1',
        # bash_command='cd /dbt && dbt seed --profiles-dir .',
        env={
            # commented out As we don't need this
            # 'dbt_user': '{{ var.value.dbt_user }}',
            # 'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag
    )

task_1