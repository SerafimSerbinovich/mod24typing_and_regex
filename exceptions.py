class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughDataError(BaseError):
    message = 'Не все поля заполнены'


class UnknownMethodError(BaseError):
    message = 'Неизвестный метод'


class UnknownFilenameError(BaseError):
    message = 'Неизвестный файл с данными'
