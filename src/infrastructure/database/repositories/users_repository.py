
from datetime import datetime

from src.infrastructure.database.entities.users import Users as UsersEntity
from src.infrastructure.database.settings.connection import DBConnectionHandler


class UserRepository:
    """_summary_
        User repository
    """

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, birthdate: datetime) -> None:
        """_summary_
        Insert user
        Args:
            first_name (str): _description_
            last_name (str): _description_
            birthdate (DateTime): _description_

        Raises:
            exception: _description_
        """
        with DBConnectionHandler() as database:
            if not database.session:
                return
            try:
                new_user = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    birthdate=birthdate
                )
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
