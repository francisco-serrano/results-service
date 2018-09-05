import sqlite3


class ResultsDatabase:
    def __init__(self, db_dir):
        self.connection = sqlite3.connect(db_dir)
        self.cursor = self.connection.cursor()
        self.query_consulta_datos = 'select * from "{}" where "integrante" = "{}"'
        self.query_consulta_columnas = 'pragma table_info("{}")'

    def get_row(self, table_name, member_name):
        self.cursor.execute(self.query_consulta_datos.format(table_name, member_name))
        return self.cursor.fetchall()

    def get_columns(self, table_name):
        return list(map(lambda x: x[1], self.cursor.execute(self.query_consulta_columnas.format(table_name))))

    def close_connection(self):
        self.connection.close()