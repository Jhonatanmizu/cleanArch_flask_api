from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime

from src.infrastructure.database.settings.base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(254))
    last_name: Mapped[str] = mapped_column(String(254))
    birthdate: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self) -> str:
        fullname = f'{self.first_name} ${self.last_name}'
        return f"User(id={self.id!r}, fullname={fullname!r})"
