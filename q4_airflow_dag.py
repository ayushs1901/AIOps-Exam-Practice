from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def collect_metrics():
    print("Collecting metrics")


def process_metrics():
    print("Processing metrics")


def detect_anomaly():
    print("Detecting anomalies")


def generate_report():
    print("Generating report")


with DAG(
    dag_id="aiops_workflow",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics
    )

    task2 = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics
    )

    task3 = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly
    )

    task4 = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    task1 >> task2 >> task3 >> task4