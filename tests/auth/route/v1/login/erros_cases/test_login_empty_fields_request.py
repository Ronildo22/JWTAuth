from tests.auth.route.v1.login.utils_url_route import URL

UNPROCESSABLE_ENTITY = 422


def test_login_endpoint_with_empty_values_username_and_password_reponse_422(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with empty username and password
        fields
    THEN:
        - The response status code should be 422 Unprocessable Entity
    """

    payload = {'username': '', 'password': ''}

    response = client_http.post(URL, json=payload)

    assert response.status_code == UNPROCESSABLE_ENTITY


def test_login_endpoint_with_empty_values_username_and_password_full_reponse(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with empty username and password
        fields
    THEN:
        - The response should contain an error message indicating both fields
        cannot be empty
        - The error message should be:
            "username: Value error, username cannot be empty"
            "password: Value error, password cannot be empty"
        - The message should be "Invalid Input Data"
    """

    payload = {'username': '', 'password': ''}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        'error': [
            'username: Value error, username cannot be empty',
            'password: Value error, password cannot be empty',
        ],
        'message': 'Invalid Input Data',
    }


def test_login_endpoint_with_empty_username(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with an empty username field
    THEN:
        - The response should contain an error message indicating the username
        cannot be empty
        - The error message should be "username: Value error, username cannot
        be empty"
    """

    payload = {'username': '', 'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert (
        'username: Value error, username cannot be empty' in error_field_data
    )


def test_login_endpoint_with_empty_password(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with an empty password field
    THEN:
        - The response should contain an error message indicating the password
        cannot be empty
        - The error message should be "password: Value error, password cannot
        be empty"
    """

    payload = {'username': 'testusername', 'password': ''}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert (
        'password: Value error, password cannot be empty' in error_field_data
    )


def test_login_endpoint_with_empty_values_username_and_password(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with empty username and password
        fields
    THEN:
        - The response should contain a message indicating invalid input data
        - The message should be "Invalid Input Data"
    """

    payload = {'username': '', 'password': ''}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', None)

    assert message_error_data == 'Invalid Input Data'
