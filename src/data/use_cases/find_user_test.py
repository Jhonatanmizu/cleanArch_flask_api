
from src.data.use_cases.find_user import FindUser
from src.infrastructure.database.repositories.users_repository import \
    UserRepository


def test_find_user_by_id(mocker):
    """_summary_
        Test find user by id.
    """
    repository = UserRepository()
    find_user = FindUser(repository)
    # mock_user_repository = mocker.patch.object(
    #     UserRepository, "find_user_by_id")
    # mock_user_repository.return_value = {"id": 1, "first_name": "John"}

    # find_user = FindUser()
    # result = find_user.find_by_id(1)

    # assert result == {"id": 1, "first_name": "John"}
    # mock_user_repository.assert_called_once_with(1)
