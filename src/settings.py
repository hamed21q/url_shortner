from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings

PROJECT_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    ENVIRONMENT: Literal["PYTEST", "PRODUCTION", "MIGRATION"] = "PRODUCTION"
    DB_HOST: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    TEST_DB_NAME: str
    DB_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int
    TEST_REDIS_DB: int
    REDIS_DB: int

    class Config:
        env_file = f"{PROJECT_DIR}/.env"
        case_sensitive = True
        extra = "allow"

    def construct_postgres_url(self, driver_name='postgresql+asyncpg'):
        return "{}://{}:{}@{}:{}/{}".format(
            driver_name,
            self.DB_USERNAME,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_PORT,
            self.TEST_DB_NAME if self.ENVIRONMENT == "PYTEST" else self.DB_NAME
        )

    def construct_redis_url(self):
        return "redis://{}:{}/{}".format(
            self.REDIS_HOST,
            self.REDIS_PORT,
            self.TEST_REDIS_DB if self.ENVIRONMENT == "PYTEST" else self.REDIS_DB
        )


setting = Settings()
