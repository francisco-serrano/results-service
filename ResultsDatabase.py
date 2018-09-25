import sqlite3


class ResultsDatabase:
    def __init__(self, db_dir):
        self.connection = sqlite3.connect(db_dir)
        self.cursor = self.connection.cursor()
        self.query_consulta_datos_integrante = 'select * from "{}" where "integrante" is "{}"'
        self.query_consulta_datos_todos = 'select * from "{}"'
        self.query_consulta_columnas = 'pragma table_info("{}")'
        self.query_consulta_tablas = 'select name from sqlite_master where type = "table"'

    def find_one(self, table_name, member_name):
        self.cursor.execute(self.query_consulta_datos_integrante.format(table_name, member_name))
        return self.cursor.fetchall()

    def find_all(self, table_name):
        self.cursor.execute(self.query_consulta_datos_todos.format(table_name))
        return self.cursor.fetchall()

    def get_columns(self, table_name):
        return list(map(lambda x: x[1], self.cursor.execute(self.query_consulta_columnas.format(table_name))))

    def get_tables(self):
        self.cursor.execute(self.query_consulta_tablas)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
