from tests.auth.route.v1.refresh.utils_url_route import URL

UNAUTHORIZED = 401


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_invalid_refresh_token_reponse_401(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with an invalid JWT token in the
        request body
    THEN:
        - The response status code should be 401 Unauthorized
    """

    payload = {'refresh_token': 'test_token'}

    response = client_http.post(URL, json=payload)

    assert response.status_code == UNAUTHORIZED


# TODO
# create real and valid data for test
def test_refresh_endpoint_with_invalid_refresh_token(
    client_http,
):
    """
    GIVEN:
        - An HTTP client
        - A refresh endpoint URL
    WHEN:
        - The client sends a POST request with an invalid JWT token in the
        request body
    THEN:
        - The response should contain an error message indicating the token is
        invalid
        - The message should be "Invalid token"
    """

    payload = {'refresh_token': 'test_token'}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get('message', None)

    assert message_error_data == 'Invalid token'
