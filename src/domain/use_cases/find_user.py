from abc import ABC, abstractmethod


class FindUser(ABC):

    @abstractmethod
    def find_by_id(self, user_id: int) -> dict: pass

    @abstractmethod
    def find_by_first_name(self, first_name: str) -> dict: pass
