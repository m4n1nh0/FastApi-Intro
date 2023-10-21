from sqlalchemy import Column, DateTime, func, String, Integer, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_utils import EmailType

from database.db import Base, database_commit


class User(Base):
    """"Classe de usuario para gestão de banco."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
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
        result = await self.session.execute(query).scalars().unique().all()

        return result

    async def get_by_username(self, username: str) -> User:
        query = select(User).where(User.username == username)
        result = await self.session.execute(query).scalars().first()

        return result

    async def insert(self, user: dict) -> None:
        user_created = User(**user)
        await database_commit(self.session, user_created)
