from exceptions import BaseException

class InvalidInput(BaseException):
    def __init__(self, message):
        super().__init__(message)

class NotFoundModel(BaseException):
    def __init__(self, message):
        super().__init__(message)

class AlreadyExists(BaseException):
    def __init__(self, message):
        super().__init__(message)

