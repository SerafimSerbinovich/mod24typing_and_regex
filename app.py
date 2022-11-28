import os

from constants import BASE_DIR
from flask import Flask, request, jsonify
from utils import dict_of_utils, log_generator

app = Flask(__name__)


@app.post("/perform_query")
def perform_query():
    file_name = request.args.get('file_name')
    cmd1 = request.args.get('cmd1')
    value1 = request.args.get('value1')
    cmd2 = request.args.get('cmd2')
    value2 = request.args.get('value2')

    if None in (file_name, cmd1, value1, cmd2, value2):
        return 'Не все поля заполнены', 400

    if cmd1 not in dict_of_utils or cmd2 not in dict_of_utils:
        return 'Неизвестная функция', 400

    if not os.path.exists(BASE_DIR + '/data/' + file_name):
        return 'Файл не найден', 400

    default_generator = log_generator()

    first_func = dict_of_utils.get(cmd1)
    second_func = dict_of_utils.get(cmd2)

    first_res = first_func(value1, default_generator)
    second_res = second_func(value2, first_res)

    return jsonify(list(second_res))


if __name__ == '__main__':
    app.run()
