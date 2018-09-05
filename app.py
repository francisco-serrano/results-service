from flask import Flask, jsonify, request

from properties import properties
from ResultsDatabase import ResultsDatabase

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

db = ResultsDatabase(properties['db_file'])


def format_output(raw_result, columns):
    def format_tuple(columns_inner, raw_tuple):
        processed_tuple = {}
        for column, value in zip(columns_inner, raw_tuple):
            processed_tuple[column] = value

        return processed_tuple

    return jsonify(list(map(lambda row: format_tuple(columns, row), raw_result)))


@app.route('/<tablename>', methods=['GET'])
def get_all_users(tablename):
    raw_result = db.find_all(tablename)
    columns = db.get_columns(tablename)

    return format_output(raw_result, columns)


@app.route('/<tablename>/<username>', methods=['GET'])
def get_user(tablename, username):
    raw_result = db.find_one(tablename, username)
    columns = db.get_columns(tablename)

    return format_output(raw_result, columns)


if __name__ == '__main__':
    app.run()
