from tests.auth.route.v1.login.utils_url_route import URL


def test_login_endpoint_with_no_body_reponse_422(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with empty body
    THEN:
        - The response status code should be 422 Unprocessable Entity
    """

    payload = {}

    response = client_http.post(URL, json=payload)

    UNPROCESSABLE_ENTITY = 422

    assert response.status_code == UNPROCESSABLE_ENTITY


def test_login_endpoint_with_no_body_full_reponse(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with no request body
    THEN:
        - The response should contain an error message indicating both fields
        cannot be empty
        - The error message should be:
            "username: Field required"
            "password: Field required"
        - The message should be "Invalid Input Data"
    """

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        'error': ['username: Field required', 'password: Field required'],
        'message': 'Invalid Input Data',
    }


# TODO
# create fake data for test
def test_login_endpoint_with_no_username_field(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with no username field
    THEN:
        - The response should contain an error message indicating the username
        field is required
    """

    payload = {'password': 'testpassword'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert 'username: Field required' in error_field_data


# TODO
# create fake data for test
def test_login_endpoint_with_no_password_field(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with no password field
    THEN:
        - The response should contain an error message indicating the password
    """

    payload = {'username': 'testusername'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert 'password: Field required' in error_field_data


# TODO
# create fake data for test
def test_login_endpoint_with_no_body(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A login endpoint URL
    WHEN:
        - The client sends a POST request with an empty request body
    THEN:
        - The response should contain a message indicating invalid input data
    """

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', None)

    assert message_error_data == 'Invalid Input Data'
