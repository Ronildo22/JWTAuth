from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError,
    JWTInvalidTokenError,
)
from src.auth.service.jwt import create_refresh_token, decode_token
from tests.auth.route.v1.refresh.utils_url_route import URL

CREATED = 201


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_valid_refresh_token_response_201(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with a valid refresh token
    THEN:
        - The response status code should be 201 Created
    """

    refresh_token = create_refresh_token(data='testuser')
    payload = {'refresh_token': refresh_token}

    response = client_http.post(URL, json=payload)

    assert response.status_code == CREATED


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_refresh_endpoint_with_valid_refresh_token_response_access_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with a valid refresh token
    THEN:
        - The response should contain an access token
        - The access token should be a valid JWT token
    """

    response_test = None
    refresh_token = create_refresh_token(data='testuser')
    payload = {'refresh_token': refresh_token}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get('access_token', '')

    try:
        decode_token(access_token)
        response_test = True

    except (JWTExpiredSignatureError, JWTInvalidTokenError):
        response_test = False

    assert response_test


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_valid_refresh_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with a valid refresh token
    THEN:
        - The response should contain a message indicating the token was
        refreshed successfully
        - The message should be "Token refreshed successfully
    """

    refresh_token = create_refresh_token(data='testuser')
    payload = {'refresh_token': refresh_token}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get('message', None)

    assert access_token == 'Token refreshed successfully'


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_valid_refresh_token_response_token_type(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with a valid refresh token
    THEN:
        - The response should contain a token type
        - The token type should be "Bearer"
    """

    refresh_token = create_refresh_token(data='testuser')
    payload = {'refresh_token': refresh_token}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    token_type = data_response.get('token_type', None)

    assert token_type == 'Bearer'
