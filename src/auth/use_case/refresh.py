import jwt
from pydantic import ValidationError

from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError, JWTInvalidTokenError)
from src.auth.service.jwt import create_access_token, verify_jwt_token
from src.auth.use_case.dto.refresh_input import RefreshInputDTO
from src.exceptions.input_data_error import InputDataError
from src.http_dto.http_request import HttpRequestDTO


def refresh_token(http_request_dto: HttpRequestDTO):

    try:

        # Validate the input data
        refresh_data = RefreshInputDTO(**http_request_dto.body)

        payload = verify_jwt_token(refresh_data.refresh_token)

        data = payload["sub"]

        # Aqui você pode validar se esse refresh_token ainda é válido no DB (opcional, mas ideal)

        new_access_token = create_access_token(data)
        return {
            "status_code": 201,
            "body": {
                "access_token": new_access_token,
                "token_type": "Bearer",
                "message": "Token refreshed successfully",
            },
        }

    except ValidationError as e:
        raise InputDataError(error=e)

    except jwt.ExpiredSignatureError:
        raise JWTExpiredSignatureError(message="Token has expired")

    except jwt.InvalidTokenError:
        raise JWTInvalidTokenError(message="Invalid JWT token")
