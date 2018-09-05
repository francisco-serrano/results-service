from flask import Flask, jsonify, request

from properties import properties
from ResultsDatabase import ResultsDatabase

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

db = ResultsDatabase(properties['db_file'])


def format_tuple(columns, raw_tuple):
    processed_tuple = {}
    for column, value in zip(columns, raw_tuple):
        processed_tuple[column] = value

    return processed_tuple


@app.route('/', methods=['GET'])
def hello_world():
    tablename = request.args.get('tablename', type=str)
    username = request.args.get('username', type=str)

    raw_result = db.get_row(tablename, username)
    columns = db.get_columns(tablename)

    processed_result = list(map(lambda row: format_tuple(columns, row), raw_result))

    return jsonify(processed_result)


if __name__ == '__main__':
    app.run()
