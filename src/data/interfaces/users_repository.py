from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.domain.models.users import Users


class UserRepository(ABC):
    """
        User repository interface
    """
    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, birthdate: datetime):
        """_summary_
        Insert user
        Args:
            first_name (str): _description_
            last_name (str): _description_
            birthdate (DateTime): _description_

        Raises:
            exception: _description_
        """

    @abstractmethod
    def find_user_by_id(self, _id: int) -> List[Users] | None:
        """_summary_

            Find user by id
        Args:
            _id (int): _description_

        Raises:
            exception: _description_

        Returns:
            UsersEntity | None: _description_
        """

    @abstractmethod
    def find_user_by_first_name(
            self, first_name: str) -> List[Users] | None:
        """_summary_
            Find user by first_name and last_name
        Args:
            first_name (str): _description_

        Raises:
            exception: _description_

        Returns:
            UsersEntity | None: _description_
        """
