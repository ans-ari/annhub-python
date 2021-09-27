class PredictException(BaseException):
    """Raised when the model can not predict"""
    ...


class ModelLoadException(BaseException):
    """Raised when the model can not be loaded correctly"""
    ...


class InvalidInputException(BaseException):
    """Raised when the data input does not meet predefined constraints"""
    ...
