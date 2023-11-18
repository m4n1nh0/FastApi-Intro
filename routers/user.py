from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_connection
from models.user import UserDTO
from schemas.user import UserInsertSchema, UserResponse, UserUpdateSchema
from utils.common import http_exception

router = APIRouter(tags=["Users"])


@router.get("/v1/users")
async def users(auth_jwt: AuthJWT = Depends(),
                session: AsyncSession = Depends(get_connection)) -> UserResponse:
    """Get all users."""
    auth_jwt.jwt_required()

    user_dto = UserDTO(session)
    result = await user_dto.get_all_users()

    return UserResponse(users=result)


@router.post("/v1/user", summary="User data insert",
             description="Rota para criação de novos usuarios do sistema academico")
async def insert_user(
        user: UserInsertSchema,
        jwt_auth: AuthJWT = Depends(),
        session: AsyncSession = Depends(get_connection)):
    jwt_auth.jwt_required()

    user_schema = user.dict()
    user_dto = UserDTO(session)
    await user_dto.insert(user_schema)

    return {"Usuario Criado Com Sucesso"}


@router.put("/v1/user/{user_id}", summary="User data update",
            description="Rota para atualização de dados dos usuários")
async def update_user(
        user_id: int,
        user: UserUpdateSchema,
        jwt_auth: AuthJWT = Depends(),
        session: AsyncSession = Depends(get_connection)):
    jwt_auth.jwt_required()

    user_schema = user.dict()
    user_dto = UserDTO(session)
    user_data = user_dto.get_by_id(user_id)
    if user_data:
        await user_dto.update(user_id, user_schema)
    else:
        raise http_exception("Usuario inexistente", 401)

    return {"Usuario Atualizado Com Sucesso"}


@router.delete("/v1/user/{user_id}", summary="User data delete",
               description="Rota para deletar usuario")
async def update_user(
        user_id: int,
        jwt_auth: AuthJWT = Depends(),
        session: AsyncSession = Depends(get_connection)):
    jwt_auth.jwt_required()

    user_dto = UserDTO(session)
    user_data = user_dto.get_by_id(user_id)
    if user_data:
        await user_dto.delete(user_id)
    else:
        raise http_exception("Usuario inexistente", 401)

    return {"Usuario deletado Com Sucesso"}
