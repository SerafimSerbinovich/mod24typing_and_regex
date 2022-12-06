import os
from typing import Iterable, Callable

from constants import BASE_DIR
from flask import Flask, request, jsonify, Response
from utils import dict_of_utils, log_generator

app = Flask(__name__)


@app.post("/perform_query")
def perform_query() -> Response:
    file_name: str = request.args['file_name']
    cmd1: str = request.args['cmd1']
    value1: str = request.args['value1']
    cmd2: str = request.args['cmd2']
    value2: str = request.args['value2']

    if None in (file_name, cmd1, value1, cmd2, value2):
        return Response('Не все поля заполнены', 400)

    if cmd1 not in dict_of_utils or cmd2 not in dict_of_utils:
        return Response('Неизвестная функция', 400)

    if not os.path.exists(BASE_DIR + '/data/' + file_name):
        return Response('Файл не найден', 400)

    default_generator: Iterable = log_generator()

    first_func: Callable = dict_of_utils[cmd1]
    second_func: Callable = dict_of_utils[cmd2]

    first_res = first_func(value1, default_generator)
    second_res = second_func(value2, first_res)

    res_list = list(second_res)

    return jsonify(res_list)


if __name__ == '__main__':
    app.run()


