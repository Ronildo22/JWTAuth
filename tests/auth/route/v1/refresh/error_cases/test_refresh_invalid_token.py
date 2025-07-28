from tests.auth.route.v1.refresh.utils_url_route import URL

# TODO
# create real and valid data for test
def test_refresh_given_valid_request_body_but_invalid_token_jwt_then_response_status_code_401(
    client_http,
):

    payload = {"refresh_token": "test_token"}

    response = client_http.post(URL, json=payload)

    assert response.status_code == 401


# TODO
# create real and valid data for test
def test_refresh_given_invalid_refresh_token_then_response_message_error(
    client_http,
):

    payload = {"refresh_token": "test_token"}

    response = client_http.post(URL, json=payload)
    data_response = response.json
    message_error_data = data_response.get("message", None)

    assert message_error_data == "Invalid token"