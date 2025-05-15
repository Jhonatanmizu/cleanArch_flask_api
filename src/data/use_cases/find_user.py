from typing import List

from src.data.interfaces.users_repository import \
    UserRepository as UserRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.find_user import FindUser as FindUserInterface


class FindUser(FindUserInterface):
    """_summary_
        FindUser use case implementation.
    """

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def find_by_id(self, user_id: int) -> List[Users] | None:
        """_summary_
            Find user by id.
        """
        result: List[Users] | None = self.user_repository.find_user_by_id(
            user_id)
        return result

    def find_by_first_name(self, first_name: str) -> List[Users] | None:
        """_summary_
            Find user by first name.
        """
        result: List[Users] | None = self.user_repository.find_user_by_first_name(
            first_name)
        return result
