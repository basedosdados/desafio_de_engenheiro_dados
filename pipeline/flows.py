from prefect import Flow
from tasks import materialize_table, print_table
from schedules import every_month

with Flow(name="planos") as flow:
    dbt_task = materialize_table()

    print_table(upstream_tasks=[dbt_task])

flow.run()