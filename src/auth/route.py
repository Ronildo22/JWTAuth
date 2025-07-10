from flask import Blueprint, jsonify, request

from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError, JWTInvalidTokenError)
from src.auth.use_case.login import login
from src.auth.use_case.refresh import refresh_token
from src.exceptions.input_data_error import InputDataError
from src.http_dto.http_request import HttpRequestDTO
from src.http_dto.http_response import HttpResponseDTO

bp_auth = Blueprint("bp_jwt_auth", __name__)


@bp_auth.post("/auth/login")
def login_route():

    try:

        http_request_dto = HttpRequestDTO(
            method=request.method,
            url=request.url,
            headers=dict(request.headers),
            body=request.json,
        )

        response = login(http_request_dto=http_request_dto)

        http_response_dto = HttpResponseDTO(
            status_code=response["status_code"], body=response["body"]
        )

    except InputDataError as e:
        http_response_dto = HttpResponseDTO(
            status_code=400, body={"error": e.error, "message": e.message}
        )

    except Exception:
        http_response_dto = HttpResponseDTO(
            status_code=500, body={"error": "Internal Server Error"}
        )

    return (
        jsonify(http_response_dto.to_dict()["body"]),
        http_response_dto.status_code,
        http_response_dto.headers,
    )


@bp_auth.post("/auth/refresh")
def refresh_route():

    try:

        http_request_dto = HttpRequestDTO(
            method=request.method,
            url=request.url,
            headers=dict(request.headers),
            body=request.json,
        )

        response = refresh_token(http_request_dto=http_request_dto)

        http_response_dto = HttpResponseDTO(
            status_code=response["status_code"], body=response["body"]
        )

    except InputDataError as e:
        http_response_dto = HttpResponseDTO(
            status_code=400, body={"error": e.error, "message": e.message}
        )

    except JWTInvalidTokenError as e:
        http_response_dto = HttpResponseDTO(
            status_code=401, body={"error": e.message}
        )

    except JWTExpiredSignatureError as e:

        http_response_dto = HttpResponseDTO(
            status_code=401, body={"error": e.message}
        )

    except Exception:
        http_response_dto = HttpResponseDTO(
            status_code=500, body={"error": "Internal Server Error"}
        )

    return (
        jsonify(http_response_dto.to_dict()["body"]),
        http_response_dto.status_code,
        http_response_dto.headers,
    )


@bp_auth.post("/auth/logout")
def logout_route(): ...
