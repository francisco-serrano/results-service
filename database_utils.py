import pandas as pd
import sqlite3

from properties import properties


def load_classification_into_db(db_file, csv_file, table_name):
    connection = sqlite3.connect(db_file)

    df = pd.read_csv(csv_file, sep=',')
    df.to_sql(table_name, connection)

    connection.commit()
    connection.close()


load_classification_into_db(
    properties['db_file'],
    properties['csv_file'],
    properties['table_name']
)
