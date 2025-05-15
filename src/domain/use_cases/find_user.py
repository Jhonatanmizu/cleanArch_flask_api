from abc import ABC, abstractmethod
from typing import List

from src.domain.models.users import Users


class FindUser(ABC):
    """_summary_
        FindUser use case interface.
    """
    @abstractmethod
    def find_by_id(self, user_id: int) -> List[Users] | None:
        """_summary_
            Find user by id.
        """

    @abstractmethod
    def find_by_first_name(self, first_name: str) -> List[Users] | None:
        """_summary_
            Find user by first name.
        """
