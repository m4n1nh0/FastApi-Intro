""""Database Connection"""
from prettyconf import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

postgres_url = config("BANCO_AUTH", default=None)

Base = declarative_base()

async_engine = create_async_engine(postgres_url, future=True)

session_local = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_connection():
    async with session_local() as session:
        try:
            yield session
        finally:
            await session.close()


async def database_commit(session, model) -> None:
    """Generalized commit for used in the system."""
    try:
        session.add(model)
        await session.commit()
        await session.refresh(model)
    except SQLAlchemyError as err:
        print(err)
        await session.rollback()
