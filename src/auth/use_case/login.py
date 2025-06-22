from pydantic import ValidationError

from src.auth.service.jwt import create_access_token, create_refresh_token
from src.auth.use_case.dto.login_input import LoginInputDTO
from src.exceptions.input_data_error import InputDataError
from src.http_dto.http_request import HttpRequestDTO


def login_service(http_request_dto: HttpRequestDTO):

    try:

        # Validate the input data
        login_data = LoginInputDTO(**http_request_dto.body)

        token_access_token = create_access_token(data=login_data.username)
        token_refresh_token = create_refresh_token(data=login_data.username)

        return {
            "status_code": 201,
            "body": {
                "access_token": token_access_token,
                "refresh_token": token_refresh_token,
                "token_type": "Bearer",
                "message": "Login successful",
            },
        }

    except ValidationError as e:
        raise InputDataError(error=e)
