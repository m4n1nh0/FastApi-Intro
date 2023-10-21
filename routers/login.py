"""Login routes implementation."""

from fastapi import APIRouter, Depends, Request
from fastapi_jwt_auth import AuthJWT
from schemas.login import LoginSchema
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_connection
from domain.token import (get_token, get_sub_authentication, create_token,
                          redis_token)
from models.user import UserDTO
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

# Variable for creating the root login
router = APIRouter(tags=["Login"])


@router.post("/v1/login")
async def login(user_login: LoginSchema,
                auth_jwt: AuthJWT = Depends(),
                session: AsyncSession = Depends(get_connection)) -> dict:
    """System access."""
    user_data = await UserDTO(session).get_by_username(user_login.username)

    if user_data is not None:
        token_data = {"detail": "Token Gerado",
                      "access_token": await create_token(
                          user=user_data, auth_jwt=auth_jwt),
                      "refresh_token": await create_token(
                          user=user_data, auth_jwt=auth_jwt, access=False)}

        return token_data
    else:
        return {"detail": "Usuario invalido"}


@router.post("/v1/refresh")
async def refresh(request: Request, auth_jwt: AuthJWT = Depends(),
                  session: AsyncSession = Depends(get_connection)) -> dict:
    """JWT token update."""
    auth_jwt.jwt_refresh_token_required()

    token = get_token(request)

    username = get_sub_authentication(token, auth_jwt)

    user_data = await UserDTO(session).get_by_username(username)

    new_access_token = await create_token(
        user=user_data, auth_jwt=auth_jwt)

    return {"create_new_token": True,
            "access_token": new_access_token}


@router.post("/v1/access_revoke")
def access_revoke(auth_jwt: AuthJWT = Depends()) -> dict:
    """Token storage is done in REDIS set with the value true for revoked."""
    auth_jwt.jwt_required()
    jti_access = auth_jwt.get_raw_jwt()['jti']

    redis_token(jti_access, ACCESS_TOKEN_EXPIRE_MINUTES)

    return {"detail": "Logout realizado com sucesso"}


@router.post("/v1/refresh_revoke")
def refresh_revoke(auth_jwt: AuthJWT = Depends()) -> dict:
    """Token storage is done in REDIS set with the value true for revoked."""
    auth_jwt.jwt_refresh_token_required()

    jti_access = auth_jwt.get_raw_jwt()['jti']

    redis_token(jti_access, ACCESS_TOKEN_EXPIRE_MINUTES)

    return {"detail": "Logout realizado com sucesso"}
