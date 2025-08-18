from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError,
    JWTInvalidTokenError,
)
from src.auth.service.jwt import decode_token
from tests.auth.route.v1.login.utils_url_route import URL

CREATED = 201


# TODO
# create real and valid data for test
def test_login_endpoint_with_valid_username_password_reponse_201(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with valid username and password
    THEN:
        - The response status code should be 201 Created
    """

    payload = {'username': 'testuser', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)

    assert response.status_code == CREATED


# TODO
# create real and valid data for test
def test_login_endpoint_with_valid_username_password(
    client_http,
):
    """GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with valid username and password
    THEN:
        - The response should contain a success message indicating the login
        was successful
    """

    payload = {'username': 'testuser', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_success = data_response.get('message', None)

    assert message_success == 'Login successful'


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_endpoint_with_valid_username_password_reponse_access_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with valid username and password
    THEN:
        - The response should contain an access token that is a valid JWT token
        - The access token should be decoded successfully without errors
    """

    response_test = None
    payload = {'username': 'testuser', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get('access_token', None)

    try:
        decode_token(access_token)
        response_test = True

    except (JWTExpiredSignatureError, JWTInvalidTokenError):
        response_test = False

    assert response_test


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_endpoint_with_valid_username_password_reponse_refresh_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with valid username and password
    THEN:
        - The response should contain a refresh token that is a valid JWT token
        - The refresh token should be decoded successfully without errors
    """

    response_test = None
    payload = {'username': 'testuser', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    refresh_token = data_response.get('refresh_token', None)

    try:
        decode_token(refresh_token)
        response_test = True

    except (JWTExpiredSignatureError, JWTInvalidTokenError):
        response_test = False

    assert response_test


# TODO
# create real and valid data for test
def test_login_endpoint_with_valid_username_password_reponse_token_type(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with valid username and password
    THEN:
        - The response should contain a token type of 'Bearer'
    """

    payload = {'username': 'testuser', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    token_type = data_response.get('token_type', None)

    assert token_type == 'Bearer'
