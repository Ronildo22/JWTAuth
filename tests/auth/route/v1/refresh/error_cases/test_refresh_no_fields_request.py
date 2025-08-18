from tests.auth.route.v1.refresh.utils_url_route import URL

UNPROCESSABLE_ENTITY = 422


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_no_body_reponse_422(
    client_http,
):
    """'
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with no body
    THEN:
        - The response status code should be 422 Unprocessable Entity
    """

    payload = {}

    response = client_http.post(URL, json=payload)

    assert response.status_code == UNPROCESSABLE_ENTITY


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_no_body_full_reponse(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with an empty request body
    THEN:
        - The response should contain an error message indicating the
        refresh_token field is required
        - The error message should be:
            "refresh_token: Field required"
        - The message should be "Invalid Input Data"
    """

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json

    assert data_response == {
        'error': ['refresh_token: Field required'],
        'message': 'Invalid Input Data',
    }


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_no_refresh_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with no refresh_token field
    THEN:
        - The response should contain an error message indicating the
        refresh_token field is required
        - The error message should be:
            "refresh_token: Field required
    """

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    error_field_data = data_response.get('error', [])

    assert 'refresh_token: Field required' in error_field_data


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_no_body(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with an empty request body
    THEN:
        - The response should contain a message indicating invalid input data
        - The message should be "Invalid Input Data
    """

    payload = {}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', None)

    assert message_error_data == 'Invalid Input Data'
