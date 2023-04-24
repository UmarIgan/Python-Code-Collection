import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file("/path/to/file.json")
client = bigquery.Client(credentials= credentials,project="your_project_id")

datasets = client.list_datasets()
data_map = {}
for dataset in datasets:
    tables = client.list_tables(dataset.dataset_id)
    table_dict = {}
    for table in tables:
        table_ref = client.get_table(table)
        table_size = table_ref.num_bytes
        row_count = table_ref.num_rows
        columns = {}
        for column in table_ref.schema:
            column_name = column.name
            column_field = column.field_type
            columns[column_name] = {'type': column_field, 'count': row_count}
        table_dict[table.table_id] = columns
        table_dict[table.table_id]['size'] = table_size
        table_dict[table.table_id]['count'] = row_count
    data_map[dataset.dataset_id] = table_dict

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

results = []
for dataset, tables in data_map.items():
    for table, columns in tables.items():
        for column, values in columns.items():
            if isinstance(values, dict):
                results.append({
                    'dataset_name': dataset,
                    'table_name': table,
                    'column_name': column,
                    'type': values['type'],
                    'count': values['count']
                })

# Convert the results to a pandas dataframe
df = pd.DataFrame(results)
