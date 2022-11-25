from constants import DATA_DIR


def log_generator():
    with open(DATA_DIR) as file:
        log_sting = file.readlines()
        for log in log_sting:
            yield log


def user_filter(value):
    return filter(lambda x: value in x, log_generator())


def user_map(num):
    return map(lambda string: string.split()[num], log_generator())


def user_unique():
    listt = []
    for string in log_generator():
        if string not in listt:
            listt.append(string)
            yield string


def user_sort(order):
    reverse = None

    if order == 'asc':
        reverse = False
    elif order == 'desc':
        reverse = True

    for string in sorted(log_generator(), reverse=reverse):
        yield string
    # return sorted(log_generator(), reverse=reverse)


def user_limit(num):
    counter = 1
    for string in log_generator():
        if counter > num:
            break

        counter += 1

        yield string


dict_of_utils = {
    'filter': user_filter,
    'map': user_map,
    'unique': user_unique,
    'sort': user_sort,
    'limit': user_limit
}