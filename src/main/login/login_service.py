from src.utils.auth_utils.jwt import jwt_create
from src.utils.dto_utils.http_dto.http_request import HttpDTO


def login_service(http_dto: HttpDTO): ...


# http_dto.request_data
