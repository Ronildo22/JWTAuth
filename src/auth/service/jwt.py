from datetime import datetime, timedelta, timezone

import jwt

from src.auth.service.exceptions.jwt_exceptions import (
    JWTExpiredSignatureError, JWTInvalidTokenError)
from src.utils.env.env import SECRET_KEY_JWT

ALGORITHM = "HS256"


def create_access_token(data: str) -> str:

    EXPIRES_ACCESS_TOKEN = timedelta(minutes=30)

    expiration = datetime.now(timezone.utc) + EXPIRES_ACCESS_TOKEN

    payload = {"sub": data, "exp": expiration}

    token = jwt.encode(payload, SECRET_KEY_JWT, algorithm=ALGORITHM)

    return token


def create_refresh_token(data: str) -> str:

    EXPIRES_REFRESH_TOKEN = timedelta(days=30)

    expiration = datetime.now(timezone.utc) + EXPIRES_REFRESH_TOKEN

    payload = {"sub": data, "exp": expiration}

    token = jwt.encode(payload, SECRET_KEY_JWT, algorithm=ALGORITHM)

    return token


def verify_jwt_token(token: str) -> dict:

    try:

        payload = jwt.decode(token, SECRET_KEY_JWT, algorithms=[ALGORITHM])

        return payload

    except jwt.ExpiredSignatureError:
        raise JWTExpiredSignatureError(message="Token has expired")

    except jwt.InvalidTokenError:
        raise JWTInvalidTokenError(message="Invalid JWT token")
