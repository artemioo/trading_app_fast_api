from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

from models.models import role
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeBase = declarative_base()

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False) # ?
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))  # ссылаемся на таблицу roles и столбец id


engine = create_async_engine(DATABASE_URL)  # точка входа SQLALCH в наше приложение
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
