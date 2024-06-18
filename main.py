from fastapi import FastAPI, Response, Request
from fastapi_redis_cache import FastApiRedisCache
from sqlalchemy.orm import Session
from src.router import url_router
from src.settings import setting

app = FastAPI()

app.include_router(url_router)
