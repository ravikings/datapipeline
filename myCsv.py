from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

df = pd.read_csv('/home/ubuntu/Desktop/dataengineering/data.csv')
for i,r in df.iterrows():
    print(r['name'])
    df.to_json('fromAirflow.JSON', orient='records')


# step -  2
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021,5,6),
    'retries': 1
}