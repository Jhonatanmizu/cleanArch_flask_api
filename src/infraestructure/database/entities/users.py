from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime

from src.infraestructure.database.settings.base import Base


class Users(Base):
    """
        Users entity
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(254))
    last_name: Mapped[str] = mapped_column(String(254))
    birthdate: Mapped[DateTime] = mapped_column(DateTime(False))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
