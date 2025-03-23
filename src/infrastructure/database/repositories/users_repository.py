
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

    @classmethod
    def find_user_by_id(cls, _id: int) -> UsersEntity | None:
        """_summary_

            Find user by id
        Args:
            _id (int): _description_

        Raises:
            exception: _description_

        Returns:
            UsersEntity | None: _description_
        """
        with DBConnectionHandler() as database:
            if not database.session:
                return None
            try:

                user = database.session.query(
                    UsersEntity).filter(UsersEntity.id == _id).first()
                return user
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def find_user_by_first_name(cls, first_name: str) -> UsersEntity | None:
        """_summary_
            Find user by first_name and last_name
        Args:
            first_name (str): _description_

        Raises:
            exception: _description_

        Returns:
            UsersEntity | None: _description_
        """
        with DBConnectionHandler() as database:
            if not database.session:
                return None
            try:

                user_query = database.session.query(
                    UsersEntity)
                user = user_query.filter(
                    UsersEntity.first_name == first_name).first()
                return user
            except Exception as exception:
                database.session.rollback()
                raise exception
