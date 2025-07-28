from tests.auth.route.v1.login.utils_url_route import URL


def test_login_given_empty_value_username_and_password_then_response_status_code_422(
    client_http,
):

    payload = {"username": "", "password": ""}

    response = client_http.post(URL, json=payload)

    assert response.status_code == 422


def test_login_given_empty_value_username_and_password_then_response_complete_message_error(
    client_http,
):

    payload = {"username": "", "password": ""}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        "error": [
            "username: Value error, username cannot be empty",
            "password: Value error, password cannot be empty",
        ],
        "message": "Invalid Input Data",
    }


def test_login_given_empty_value_username_then_response_message_error(
    client_http,
):

    payload = {"username": "", "password": "testpassword"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get("error", [])

    assert (
        "username: Value error, username cannot be empty" in error_field_data
    )


def test_login_given_empty_value_password_then_response_message_error(
    client_http,
):

    payload = {"username": "testusername", "password": ""}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get("error", [])

    assert (
        "password: Value error, password cannot be empty" in error_field_data
    )


def test_login_given_empty_value_username_and_password_then_response_message_error(
    client_http,
):

    payload = {"username": "", "password": ""}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get("message", None)

    assert message_error_data == "Invalid Input Data"
