from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator


def load_seed_task(dag_dummy: DAG) -> BashOperator:
    return BashOperator(
        task_id='load_seed_data_once',
        bash_command= 'cd /tmp && echo "hello1" >> task.txt && echo "hello task 1"',
        # bash_command='cd /dbt && dbt seed --profiles-dir .',
        env={
            # commented out As we don't need this
            # 'dbt_user': '{{ var.value.dbt_user }}',
            # 'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag_dummy
    )
    
