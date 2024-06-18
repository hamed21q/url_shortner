from typing import TYPE_CHECKING

from redis import Redis
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm.session import sessionmaker

from src.settings import setting


async_engine = create_async_engine(
    setting.construct_postgres_url(), pool_pre_ping=True, pool_size=20, max_overflow=10
)

async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

if TYPE_CHECKING:
    async_session: sessionmaker[AsyncSession]


async def get_db():
    async with async_session(expire_on_commit=False) as session:
        yield session


def redis_connection():
    return Redis(host=setting.REDIS_HOST, port=setting.REDIS_PORT, db=setting.REDIS_DB)