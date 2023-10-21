from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import UserDTO
from database.db import get_connection

router = APIRouter(tags=["Users"])


@router.get("/v1/users")
async def users(jwt_auth: AuthJWT = Depends(),
                session: AsyncSession = Depends(get_connection)):
    """Get all users."""
    jwt_auth.jwt_required()

    user_dto = UserDTO(session)
    result = await user_dto.get_all_users()

    return result


@router.post("/v1/user")
async def insert_user(
        user: dict,
        jwt_auth: AuthJWT = Depends(),
        session: AsyncSession = Depends(get_connection)):
    jwt_auth.jwt_required()
    user_dto = UserDTO(session)
    await user_dto.insert(user)

    return {"Usuario Criado Com Sucesso"}
