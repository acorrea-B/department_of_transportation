class InvalidInput(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotFoundModel(Exception):
    def __init__(self, message):
        super().__init__(message)

class AlreadyExists(Exception):
    def __init__(self, message):
        super().__init__(message)

class DataValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class UniqueViolation(Exception):
    def __init__(self, message):
        super().__init__(message)

class BDInsertError(Exception):
    def __init__(self, message):
        super().__init__(message)