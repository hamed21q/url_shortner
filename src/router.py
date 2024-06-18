import base62
from fastapi import APIRouter, Depends
from redis import Redis
from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse

from src.connection import get_db, redis_connection
from src.models import UrlModel
from src.repository import create_url, find_url_by_hash

url_router = APIRouter()
snow_flake_generator = SnowflakeGenerator(42)


@url_router.post("/")
async def shorten_url(url: str, session: AsyncSession = Depends(get_db)):
    hashed_url = base62.encode(next(snow_flake_generator))
    await create_url(
        session,
        UrlModel(
            original_url=url,
            hashed_url=hashed_url
        )
    )
    return {"hashed_url": hashed_url}


@url_router.get("/{hashed_url}")
async def get_url_by_hash(
        hashed_url: str,
        session: AsyncSession = Depends(get_db),
        redis: Redis = Depends(redis_connection)
):
    if original_url := redis.get(hashed_url):
        return RedirectResponse(original_url.decode())

    url: UrlModel = await find_url_by_hash(session, hashed_url)
    redis.set(hashed_url, url.original_url, 3600)
    return RedirectResponse(url.original_url)
