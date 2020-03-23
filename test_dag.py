from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('TestDAG', "A dummy test DAG", schedule_interval=timedelta(minutes=5))

test1 = DummyOperator(task_id="test1", dag=dag)
test2 = DummyOperator(task_id="test2", dag=dag)
test3 = DummyOperator(task_id="test3", dag=dag)

test1 >> test2 >> test3
