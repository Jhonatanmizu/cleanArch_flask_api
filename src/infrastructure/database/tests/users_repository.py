
from datetime import datetime
from typing import Dict, List

from src.domain.models.users import Users


class UsersRepositorySpy:
    """_summary_
        User repository
    """

    def __init__(self) -> None:
        self.insert_user_attributes: Dict = {}
        self.find_user_by_first_name_attributes: Dict = {}
        self.find_user_by_id_attributes: Dict = {}

    def insert_user(self, first_name: str, last_name: str, birthdate: datetime) -> None:
        """_summary_
        Insert user
        Args:
            first_name (str): _description_
            last_name (str): _description_
            birthdate (DateTime): _description_

        Raises:
            exception: _description_
        """
        self.insert_user_attributes = {"first_name": first_name,
                                       "last_name": last_name,
                                       "birthdate": birthdate}
        print(f'attributes:{self.insert_user_attributes}')
        return

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
        self.find_user_by_id_attributes = {"id": _id}
        return [
            Users(_id, "mizu", "gawa", datetime.now())
        ]

    def find_user_by_first_name(self, first_name: str) -> List[Users] | None:
        """_summary_
            Find user by first_name and last_name
        Args:
            first_name (str): _description_

        Raises:
            exception: _description_

        Returns:
            UsersEntity | None: _description_
        """
        self.find_user_by_first_name_attributes = {"first_name": first_name}
        return [
            Users(12, first_name, "gawa", datetime.now()),
            Users(13, first_name, "Jesus", datetime.now())
        ]
