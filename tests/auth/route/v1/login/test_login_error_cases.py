import json


def test_login_given_bad_format_request_body_then_response_status_code_500(client_http):

    url = "/v1/auth/login"
    payload = """
        {
            'username': 'testuser',
        }
    """

    response = client_http.post(url, json=json.dumps(payload))

    assert response.status_code == 500

def test_login_given_bad_format_request_body_then_response_message_error(client_http):

    url = "/v1/auth/login"
    payload = """
        {
            'username': 'testuser',
        }
    """

    response = client_http.post(url, json=json.dumps(payload))
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert error_field_data == "Internal Server Error"

def test_login_given_empty_request_body_then_response_status_code_400(client_http):

    url = "/v1/auth/login"
    payload = {}

    response = client_http.post(url, json=payload)

    assert response.status_code == 400

def test_login_given_empty_request_body_then_response_message_error(client_http):

    url = "/v1/auth/login"
    payload = {}

    response = client_http.post(url, json=payload)
    data_response = response.json

    assert data_response == {
        "error": [
            "username: Field required",
            "password: Field required"
        ],
        "message": "Invalid Input Data"
    }

# TODO
# create fake data for test
def test_login_given_username_field_not_provided_in_request_body_then_response_message_error(client_http):

    url = "/v1/auth/login"
    payload = {
        'password': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert "username: Field required" in error_field_data

# TODO
# create fake data for test
def test_login_given_password_field_not_provided_in_request_body_then_response_message_error(client_http):
    
    url = "/v1/auth/login"
    payload = {
        'username': 'testpassword'
    }

    response = client_http.post(url, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert "password: Field required" in error_field_data

# TODO
# create fake data for test
def test_login_given_invalid_input_data_fields_in_request_body_then_response_message_error(client_http):

    url = "/v1/auth/login"
    payload = {}

    response = client_http.post(url, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', [])

    assert message_error_data == "Invalid Input Data"
