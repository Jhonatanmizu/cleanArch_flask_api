from .connection import DBConnectionHandler


def test_connection():
    """Test connection"""
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    assert engine is not None


def test_create_database_engine():
    """Test create database engine"""
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    assert engine is not None
    assert engine.name == "mysql"
