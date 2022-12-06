import re
from typing import Generator, Iterable, Pattern, Dict, Callable, Optional

from constants import DATA_DIR


def log_generator() -> Iterable:
    with open(DATA_DIR) as file:
        log_sting = file.readlines()
        for log in log_sting:
            yield log


def user_filter(value: str, generator: Iterable) -> Iterable:
    return filter(lambda x: value in x, generator)


def user_map(num: str, generator: Iterable) -> Iterable:
    return map(lambda string: string.split()[int(num)], generator)


def user_unique(value, generator: Iterable) -> Iterable:
    listt: list[str] = []
    for string in generator:
        if string not in listt:
            listt.append(string)
            yield string


def user_sort(order: str, generator: Iterable) -> Iterable:
    reverse = None

    if order == 'asc':
        reverse = False
    else:
        reverse = True

    for string in sorted(generator, reverse=reverse):
        yield string


def user_limit(num: str, generator: Iterable) -> Iterable:
    counter: int = 1
    for string in generator:
        if counter > int(num):
            break

        counter += 1

        yield string


def regex(value: str, generator: Iterable) -> Iterable:
    pattern: Pattern = re.compile(value)
    for string in generator:
        if re.search(pattern, string):
            yield string


dict_of_utils: Dict[str, Callable] = {
    'filter': user_filter,
    'map': user_map,
    'unique': user_unique,
    'sort': user_sort,
    'limit': user_limit,
    'regex': regex
}
