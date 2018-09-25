from flask import Flask, jsonify, request
from io import StringIO

from properties import properties
from ResultsDatabase import ResultsDatabase
from database_utils import load_classification_into_db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

db = ResultsDatabase(properties['db_file'])


def format_output(raw_result, columns):
    return jsonify(list(map(lambda row: dict(zip(columns, row)), raw_result)))


@app.route('/<tablename>', methods=['GET'])
def get_all_users(tablename):
    raw_result = db.find_all(tablename)
    columns = db.get_columns(tablename)

    return format_output(raw_result, columns)


@app.route('/tables', methods=['GET'])
def get_tables():
    result = list(map(lambda x: x[0], db.get_tables()))
    return jsonify(result)


@app.route('/<tablename>', methods=['POST'])
def add_conversation(tablename):
    csv_file = StringIO(request.files['csv_file'].stream.read().decode('utf-8'))

    load_classification_into_db(properties['db_file'], csv_file, tablename)

    return jsonify(mensaje='alta de tabla realizada exitosamente')


@app.route('/<tablename>/<username>', methods=['GET'])
def get_user(tablename, username):
    raw_result = db.find_one(tablename, username)
    columns = db.get_columns(tablename)

    return format_output(raw_result, columns)


if __name__ == '__main__':
    app.run()
