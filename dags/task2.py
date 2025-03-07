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

with DAG('2_daily_transformation_analysis', default_args=default_args, schedule_interval='@once') as dag:
    task_1 = BashOperator(
        task_id='daily_transform',
        bash_command= 'echo hello2 >> task.txt && echo hello task 2',
        # bash_command='cd /dbt && dbt run --models transform --profiles-dir .',
        env={
            # Commented out as we not use
            # 'dbt_user': '{{ var.value.dbt_user }}',
            # 'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag
    )

    task_2 = BashOperator(
        task_id='daily_analysis',
        bash_command= 'echo hello3 >> task.txt && echo hello task 3',
        # bash_command='cd /dbt && dbt run --models analysis --profiles-dir .',
        env={
            'dbt_user': '{{ var.value.dbt_user }}',
            'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag
    )

    task_1 >> task_2 # Define dependencies