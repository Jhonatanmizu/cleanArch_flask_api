from datetime import datetime

from sqlalchemy import text

from src.infrastructure.database.settings.connection import DBConnectionHandler

from .users_repository import UserRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


def test_insert_user():
    """_summary_
        test insertion of the user in the database
    """
    mocked_first_name = "John"
    mocked_last_name = "Doe"
    mocked_birthdate = datetime(year=2000, month=11, day=24)
    user_repo = UserRepository()
    user_repo.insert_user(first_name=mocked_first_name,
                          last_name=mocked_last_name,
                          birthdate=mocked_birthdate)
    sql = '''
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
    '''.format(mocked_first_name, mocked_last_name)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()


def test_find_user_by_first_name():
    """_summary_
        test find the user by first_name
    """
    mocked_first_name = "John"
    mocked_last_name = "Doe"
    mocked_birthdate = datetime(year=2000, month=11, day=24)
    user_repo = UserRepository()
    user_repo.insert_user(first_name=mocked_first_name,
                          last_name=mocked_last_name,
                          birthdate=mocked_birthdate)

    registry = user_repo.find_user_by_first_name(first_name=mocked_first_name)

    assert registry is not None
    assert registry.first_name == mocked_first_name
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()


def test_find_user_by_id():
    """_summary_
        test find the user by id
    """
    mocked_id = 9999
    sql = text("""
            INSERT INTO users (id, first_name, last_name, birthdate) 
            VALUES (:id, :first_name, :last_name, :birthdate)
        """)
    connection.execute(
        sql,
        {"id": mocked_id, "first_name": "Hi",
            "last_name": "Mizu", "birthdate": datetime.now()}
    )
    connection.commit()
    user_repo = UserRepository()
    registry = user_repo.find_user_by_id(_id=mocked_id)

    assert registry is not None
    assert registry.id == mocked_id
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()
