from prefect import task
import os
from utils import log
from sqlalchemy import create_engine

@task
def materialize_table()-> None:
    os.system("cd ans; dbt run --profiles-dir .")

@task
def print_table() -> None:
    conn_string = 'postgresql://postgres:root@db:5432/basedosdados_dev'
    query = '''
    SELECT *
    FROM basedosdados_dev.public.planos_cat
    '''
    df = pd.read_sql_query(query,con=conn_string)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    log(df.to_markdown(index=False))