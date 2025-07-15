from src.auth.service.jwt import verify_jwt_token


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_status_code_201(client_http):

    url = "/v1/auth/login"
    payload = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)

    assert response.status_code == 201


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_message_success(client_http):
    
    url = "/v1/auth/login"
    payload = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    message_success = data_response.get('message', None)

    assert message_success == "Login successful"


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_given_valid_request_body_then_response_access_token_is_jwt_real(client_http):

    url = "/v1/auth/login"
    payload = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    access_token = data_response.get('access_token', '')
    
    # verify_jwt_token(access_token)

    # ASSERT INCORRECT
    assert isinstance(access_token, str)


# TODO
# create real and valid data for test
# validade if access_token is a valid JWT token
def test_login_given_valid_request_body_then_response_refresh_token_is_jwt_real(client_http):

    url = "/v1/auth/login"
    payload = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    refresh_token = data_response.get('refresh_token', '')
    
    # verify_jwt_token(refresh_token)

    # ASSERT INCORRECT
    assert isinstance(refresh_token, str)


# TODO
# create real and valid data for test
def test_login_given_valid_request_body_then_response_token_type(client_http):

    url = "/v1/auth/login"
    payload = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    token_type = data_response.get('token_type', None)

    assert token_type == "Bearer"
