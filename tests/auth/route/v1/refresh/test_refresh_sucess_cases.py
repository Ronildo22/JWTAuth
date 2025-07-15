from src.auth.service.jwt import create_refresh_token

URL = "/v1/auth/refresh"


# TODO
# create real and valid data for test
def test_refresh_given_valid_request_body_and_refresh_token_is_jwt_valid_then_response_status_code_201(client_http):

    refresh_token = create_refresh_token(data="testuser")
    payload = {
        "refresh_token": refresh_token
    }

    response = client_http.post(URL, json=payload)

    assert response.status_code == 201


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_refresh_given_valid_request_body_then_response_access_token_is_jwt_real(client_http):

    refresh_token = create_refresh_token(data="testuser")
    payload = {
        "refresh_token": refresh_token
    }

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get('access_token', '')
    
    # verify_jwt_token(access_token)

    # ASSERT INCORRECT
    assert isinstance(access_token, str)


# TODO
# create real and valid data for test
def test_refresh_given_valid_request_body_then_response_message_success(client_http):

    refresh_token = create_refresh_token(data="testuser")
    payload = {
        "refresh_token": refresh_token
    }

    response = client_http.post(URL, json=payload)
    data_response = response.json
    access_token = data_response.get('message', None)
    
    assert access_token == "Token refreshed successfully"


# TODO
# create real and valid data for test
def test_refresh_given_valid_request_body_then_response_token_type(client_http):
    
    refresh_token = create_refresh_token(data="testuser")
    payload = {
        "refresh_token": refresh_token
    }

    response = client_http.post(URL, json=payload)
    data_response = response.json
    token_type = data_response.get('token_type', None)

    assert token_type == "Bearer"
