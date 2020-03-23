from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('Test DAG', "A dummy test DAG", schedule_interval=timedelta(minutes=5))

test1 = DummyOperator(task_id="test 1", dag=dag)
test2 = DummyOperator(task_id="test 2", dag=dag)
test3 = DummyOperator(task_id="test 3", dag=dag)

test1 >> test2 >> test3
