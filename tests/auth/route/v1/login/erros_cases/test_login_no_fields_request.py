from tests.auth.route.v1.login.utils_url_route import URL


def test_login_given_no_request_body_then_response_status_code_422(
    client_http,
):

    payload = {}

    response = client_http.post(URL, json=payload)

    assert response.status_code == 422


def test_login_given_no_request_body_then_response_complete_message_error(client_http):

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        "error": ["username: Field required", "password: Field required"],
        "message": "Invalid Input Data",
    }


# TODO
# create fake data for test
def test_login_given_username_field_not_provided_in_request_body_then_response_message_error(
    client_http,
):

    payload = {"password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get("error", [])

    assert "username: Field required" in error_field_data


# TODO
# create fake data for test
def test_login_given_password_field_not_provided_in_request_body_then_response_message_error(
    client_http,
):

    payload = {"username": "testusername"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get("error", [])

    assert "password: Field required" in error_field_data


# TODO
# create fake data for test
def test_login_given_invalid_input_data_fields_in_request_body_then_response_message_error(
    client_http,
):

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get("message", None)

    assert message_error_data == "Invalid Input Data"
