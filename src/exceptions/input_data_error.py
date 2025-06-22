from pydantic import ValidationError

from src.utils.format_error_pydantic.validation_error import \
    format_error_menssage


class InputDataError(Exception):
    def __init__(self, error: ValidationError):
        self.error = format_error_menssage(error)
        self.message = "Invalid Input Data"
        super().__init__(self.message)
