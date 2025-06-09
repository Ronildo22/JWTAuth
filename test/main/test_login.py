from src.main.login.login_service import login_service


def test_login():
    """
    Test the login functionality.
    """

    payload = {"username": "test_user", "password": "test_password"}

    login_response = login_service(payload)

    assert login_service == "login suscessful"
