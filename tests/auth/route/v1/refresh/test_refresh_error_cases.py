import json


URL = "/v1/auth/refresh"


# TODO
# create real and valid data for test
def test_refresh_given_bad_format_request_body_then_response_status_code_500(client_http):
    
    payload = """
        {
            'refresh_token': 'test_token',
        }
    """

    response = client_http.post(URL, json=json.dumps(payload))

    assert response.status_code == 500


# TODO
# create real and valid data for test
def test_refresh_given_bad_format_request_body_then_response_message_error(client_http):

    payload = """
        {
            'refresh_token': 'test_token',
        }
    """

    response = client_http.post(URL, json=json.dumps(payload))
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert error_field_data == "Internal Server Error"


# TODO
# create real and valid data for test
def test_refresh_given_empty_request_body_then_response_status_code_400(client_http):

    payload = {}

    response = client_http.post(URL, json=payload)

    assert response.status_code == 400


# TODO
# create real and valid data for test
def test_refresh_given_empty_request_body_then_response_complete_message_error(client_http):

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        "error": [
            "refresh_token: Field required"
        ],
        "message": "Invalid Input Data"
    }


# TODO
# create real and valid data for test
def test_refresh_given_refresh_token_field_not_provided_in_request_body_then_response_message_error(client_http):

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert "refresh_token: Field required" in error_field_data


# TODO
# create real and valid data for test
def test_refresh_given_invalid_input_data_fields_in_request_body_then_response_message_error(client_http):

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', [])

    assert message_error_data == "Invalid Input Data"


# TODO
# create real and valid data for test
def test_refresh_given_valid_request_body_but_invalid_token_jwt_then_response_status_code_401(client_http):

    payload = {
        "refresh_token": "test_token"
    }

    response = client_http.post(URL, json=payload)

    assert response.status_code == 401
