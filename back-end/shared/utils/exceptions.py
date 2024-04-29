class InvalidInput(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotFoundModel(Exception):
    def __init__(self, message):
        super().__init__(message)

class AlreadyExists(Exception):
    def __init__(self, message):
        super().__init__(message)

