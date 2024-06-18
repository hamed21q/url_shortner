import datetime
import functools
from typing import Any, Type
from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Base, UrlModel


async def create_url(session: AsyncSession, url: UrlModel):
    session.add(url)
    await session.commit()
    await session.refresh(url)
    return url


async def find_url_by_hash(session: AsyncSession, hashed_url):
    query = select(UrlModel).where(UrlModel.hashed_url == hashed_url)
    result = await session.execute(query)
    url = result.scalar()
    if not url:
        raise NoResultFound()
    return url

