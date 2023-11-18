from sqlalchemy import Column, DateTime, func, String, Integer, select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_utils import EmailType

from database.db import Base, database_commit
from utils.common import delete_none


class User(Base):
    """"Classe de usuario para gestão de banco."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    usr_name = Column(String(100), index=True, nullable=False)
    username = Column(EmailType, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)


class UserDTO:
    """Classe de acesso aos dados de ususario."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_users(self):
        query = select(User)
        result = await self.session.execute(query)
        users_data = result.scalars().unique().all()

        return users_data

    async def get_by_id(self, pk: int) -> User:
        query = select(User).where(and_(User.id == pk))
        result = await self.session.execute(query)
        user_data = result.scalars().first()

        return user_data

    async def get_by_username(self, username: str) -> User:
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        user_data = result.scalars().first()

        return user_data

    async def insert(self, user: dict) -> None:
        user_created = User(**user)
        await database_commit(self.session, user_created)

    async def update(self, pk: int, user: dict) -> None:
        await delete_none(user)
        query = update(User).where(
            and_(User.id == pk)).values(**user)
        await self.session.execute(query)
        await self.session.commit()

    async def delete(self, pk: int) -> None:
        query = delete(User).where(
            and_(User.id == pk))
        await self.session.execute(query)
        await self.session.commit()
