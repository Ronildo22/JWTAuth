import jwt
from datetime import datetime, timedelta, timezone


def jwt_create(username: str, password: str) -> str:
    """
    Create a JWT token for the given username and password.
    """

    jwt.encode(
        {
            "username": username,
            "password": password,
            "exp": datetime.now(timezone.utc)
            + timedelta(days=1),  # Token expiration time set to 1 day
        },
        "secret_key",  # Replace with your actual secret key
    )
