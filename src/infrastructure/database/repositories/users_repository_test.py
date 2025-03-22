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
