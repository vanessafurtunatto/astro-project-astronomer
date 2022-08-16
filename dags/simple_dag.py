from asyncio import tasks
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.Python import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

with DAG(dag_id='simple_dag', schedule_interval=timedelta(hours=7), start_date=days_ago(3), 
catchup=True, max_active_runs=2) as dag:
    tasks_1 = DummyOperator(
        task_id='task_1'
    )

