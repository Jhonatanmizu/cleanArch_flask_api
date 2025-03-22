"""Database connection"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """SqlAlchemy database connection"""

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
        """_summary_
        Create database engine
        and return it
        Args:
            self
        Returns:
            engine: database engine
        """
        self.__engine = create_engine(self.connection_string)
        return self.__engine

    def get_engine(self):
        """_summary_
        get connection engine
        Returns:
            _type_:  connection engine
        """
        return self.__engine

    def __enter__(self):
        """_summary_
        enter connection engine
        Returns:
            _type_:  self
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        """_summary_
        exit connection engine
        Returns:
            _type_:  self
        """
        if self.session:
            self.session.close()
