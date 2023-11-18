"""Token domain implementation."""

from database.redis import redis_conn
from fastapi import Request
from fastapi_jwt_auth import AuthJWT
from models.user import User

from settings import (ACCESS_TOKEN_EXPIRE_MINUTES)


async def create_token(user: User, auth_jwt: AuthJWT,
                       access: bool = True) -> str:
    """JWT token create to username."""
    jti_access = auth_jwt.get_raw_jwt()

    if jti_access is not None:
        redis_token(jti_access['jti'], ACCESS_TOKEN_EXPIRE_MINUTES)

    subject = f"{user.username}"

    user_claims = {
        "user_age": user.age,
        "user_name": user.usr_name
    }

    if access:
        access_token = auth_jwt.create_access_token(subject=subject,
                                                    algorithm="HS256",
                                                    user_claims=user_claims)
        data = f"Bearer {access_token}"
    else:
        refresh_token = auth_jwt.create_refresh_token(subject=subject,
                                                      algorithm="HS256",
                                                      user_claims=user_claims)
        data = f"Bearer {refresh_token}"

    return data


def get_sub_authentication(token: str, auth_jwt: AuthJWT) -> str:
    """Get username from token."""
    decoded = auth_jwt.get_raw_jwt(token)

    user_name = decoded["sub"]

    return user_name


def get_sub_first_access(token, auth_jwt) -> int:
    """Get username from token."""
    decoded = auth_jwt.get_raw_jwt(token)

    return decoded["sub"]


def get_token(request: Request):
    """."""
    return request.headers["Authorization"].replace("Bearer ", "")


def redis_token(jti, time: int):
    """Redis token controller."""
    redis_conn.setex(jti, time, 'true')
    redis_conn.close()
