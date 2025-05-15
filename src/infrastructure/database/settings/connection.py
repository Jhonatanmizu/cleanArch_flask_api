"""Database connection"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self):
        user = "mizu"
        password = "root"
        host = "localhost"
        port = "3306"
        database_name = "clean_architecture_db"
        self.connection_string = (
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"
        )
        self.__engine = self.__create_database_engine__()
        self.session = None

    def __create_database_engine__(self):
        self.__engine = create_engine(self.connection_string)
        return self.__engine

    def get_engine(self):

        return self.__engine

    def __enter__(self):

        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):

        if self.session:
            self.session.close()
