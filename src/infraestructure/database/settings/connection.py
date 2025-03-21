"""Database connection"""

from sqlalchemy import create_engine


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
        self.engine = self.__create_database_engine__()

    def __create_database_engine__(self):
        """_summary_
        Create database engine
        and return it
        Args:
            self
        Returns:
            engine: database engine
        """
        self.engine = create_engine(self.connection_string)
        return self.engine

    def get_engine(self):
        """Return connection engine"""
        return self.engine
