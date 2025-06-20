from src.http_dto.http_request import HttpRequestDTO


def login_service(http_request_dto: HttpRequestDTO):

    try:
        http_request_dto.body["username"]
        http_request_dto.body["password"]
    except KeyError as e:
        return {
            "status_code": 400,
            "body": {"body": f"Missing required field: {str(e)}"},
        }

    



