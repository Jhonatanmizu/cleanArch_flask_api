from src.data.use_cases.find_user import FindUser
from src.infrastructure.database.tests.users_repository import \
    UsersRepositorySpy


def test_find_user_by_first_name():
    first_name = "Mathew"
    repository = UsersRepositorySpy()
    find_user = FindUser(repository)  # type: ignore
    response = find_user.find_by_first_name(first_name)
    assert repository.find_user_by_first_name_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == 2
    assert response["attributes"] != []


def test_find_user_by_id():
    user_id = 13
    repository = UsersRepositorySpy()
    find_user = FindUser(repository)  # type: ignore
    response = find_user.find_by_id(user_id)
    assert repository.find_user_by_id_attributes["id"] == user_id
    assert response['type'] == "Users"
    assert response['count'] == 1
    assert response["attributes"] != []

def test_find_error_invalid_name():
    first_name = "Invalid name123"
    repository = UsersRepositorySpy()
    find_user = FindUser(repository) # type: ignore
    try:
        find_user.find_by_first_name(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Name is invalid"

def test_find_error_name_too_big():
    name_too_large = "nameistobigtohandleinthiscase"
    respository = UsersRepositorySpy()
    find_user = FindUser(respository) # type: ignore
    try:
        find_user.find_by_first_name(name_too_large)
        assert False
    except Exception as expection:
        assert str(expection) == "Name is too big"
