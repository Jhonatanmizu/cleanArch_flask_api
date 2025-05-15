
from datetime import datetime
from typing import Dict, List

from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes: Dict = {}
        self.find_user_by_first_name_attributes: Dict = {}
        self.find_user_by_id_attributes: Dict = {}

    def insert_user(self, first_name: str, last_name: str, birthdate: datetime) -> None:
        self.insert_user_attributes = {"first_name": first_name,
                                       "last_name": last_name,
                                       "birthdate": birthdate}
        print(f'attributes:{self.insert_user_attributes}')
        return

    def find_user_by_id(self, _id: int) -> List[Users] | None:

        self.find_user_by_id_attributes = {"id": _id}
        return [
            Users(_id, "mizu", "gawa", datetime.now())
        ]

    def find_user_by_first_name(self, first_name: str) -> List[Users] | None:

        self.find_user_by_first_name_attributes = {"first_name": first_name}
        return [
            Users(12, first_name, "gawa", datetime.now()),
            Users(13, first_name, "Jesus", datetime.now())
        ]
