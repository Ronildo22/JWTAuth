from flask import Blueprint, jsonify, request

from src.http_dto.http_request import HttpRequestDTO
from src.http_dto.http_response import HttpResponseDTO
from src.auth.use_case.login import login_service

bp_auth = Blueprint("bp_jwt_auth", __name__)


@bp_auth.post("/auth/login")
def login():

    try:
            
        http_request_dto = HttpRequestDTO(
            method=request.method,
            url=request.url,
            headers=dict(request.headers),
            body=request.json,
        )

        response = login_service(http_request_dto=http_request_dto)

        http_response_dto = HttpResponseDTO(
            status_code=response['status_code'],
            body=response['body']
        )

        return jsonify(
            {"body": http_response_dto.to_dict()['body']}
        ), http_response_dto.status_code, http_response_dto.headers
    
    except Exception:

        http_response_dto = HttpResponseDTO(
            status_code=500,
            body={"error": "Internal Server Error"}
        )

        return jsonify(
            {"body": http_response_dto.to_dict()['body']}
        ), http_response_dto.status_code, http_response_dto.headers



@bp_auth.post("/auth/logout")
def logout(): ...
