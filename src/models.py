from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UrlModel(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    original_url: Mapped[str] = mapped_column(String(256), unique=True)
    hashed_url: Mapped[str] = mapped_column(String(256), unique=True)
