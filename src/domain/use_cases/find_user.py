from abc import ABC, abstractmethod


class FindUser(ABC):
    """_summary_
        FindUser use case interface.
    """

    @abstractmethod
    def find_by_id(self, user_id: int) -> dict:
        """_summary_
            Find user by id.
        """

    @abstractmethod
    def find_by_first_name(self, first_name: str) -> dict:
        """_summary_
            Find user by first name.
        """
