from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from src.domain.models.users import Users


class UsersRepository(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str,
                    birthdate: datetime): pass

    @abstractmethod
    def find_user_by_id(self, _id: int) -> List[Users] | None: pass

    @abstractmethod
    def find_user_by_first_name(
        self, first_name: str) -> List[Users] | None: pass
