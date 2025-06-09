from flask import Blueprint, request, jsonify
from src.utils.auth_utils.jwt import jwt_create
from src.utils.dto_utils.http_dto.http_request_dto import HttpRequestDTO

bp_jwt_auth = Blueprint("bp_jwt_auth", __name__)


@bp_jwt_auth.post("/login")
def login_route():

    payload = request.get_json()

    http_request_dto = HttpRequestDTO(payload=payload)

    return jsonify(jwt), 200
