from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError, JWTInvalidTokenError)
from src.auth.service.jwt import decode_token
from tests.auth.route.v1.login.utils_url_route import URL


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_status_code_201(
    client_http,
):

    payload = {"username": "testuser", "password": "testpassword"}

    response = client_http.post(URL, json=payload)

    assert response.status_code == 201


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_message_success(
    client_http,
):

    payload = {"username": "testuser", "password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_success = data_response.get("message", None)

    assert message_success == "Login successful"


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_given_valid_request_body_then_response_access_token_is_jwt_real(
    client_http,
):

    response_test = None
    payload = {"username": "testuser", "password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get("access_token", None)

    try:

        decode_token(access_token)
        response_test = True

    except (JWTExpiredSignatureError, JWTInvalidTokenError):
        response_test = False

    assert response_test == True


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_given_valid_request_body_then_response_refresh_token_is_jwt_real(
    client_http,
):

    response_test = None
    payload = {"username": "testuser", "password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    refresh_token = data_response.get("refresh_token", None)

    try:

        decode_token(refresh_token)
        response_test = True

    except (JWTExpiredSignatureError, JWTInvalidTokenError):
        response_test = False

    assert response_test == True


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_token_type(client_http):

    payload = {"username": "testuser", "password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    token_type = data_response.get("token_type", None)

    assert token_type == "Bearer"
