# pylint: disable=broad-exception-raised

from typing import Dict, List

from src.data.interfaces.users_repository import \
    UsersRepository as UsersRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.find_user import FindUser as FindUserInterface


class FindUser(FindUserInterface):
    """_summary_
        FindUser use case implementation.
    """

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find_by_id(self, user_id: int) -> Dict:
        """_summary_
            Find user by id.
        """

        if not user_id:
            raise Exception("Missing user_id")

        results: List[Users] | None = self.__users_repository.find_user_by_id(
            user_id)
        if results is None or len(results) == 0:
            raise Exception("User does not exists")
        response = {
            "type": "Users",
            "count": len(results),
            "attributes": results
        }
        return response

    def find_by_first_name(self, first_name: str) -> Dict:
        """_summary_
            Find user by first name.
        """
        if not first_name.isalpha():
            raise Exception("Name is invalid")

        if len(first_name) > 18:
            raise Exception("Name is too big")

        results: List[Users] | None = self.__users_repository.find_user_by_first_name(
            first_name)

        if results == [] or results is None:
            raise Exception("User does not exists")
        response = {
            "type": "Users",
            "count": len(results),
            "attributes": results
        }
        return response
