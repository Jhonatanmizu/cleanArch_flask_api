from datetime import datetime

from sqlalchemy import text

from .connection import DBConnectionHandler


def test_connection():
    """ Test connection """
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    assert engine is not None


def test_create_database_engine():
    """ Test create database engine """
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    assert engine is not None
    assert engine.name == "mysql"


def test_create_user():
    """ Test create user """
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    connection = engine.connect()
    sql = text("""
            INSERT INTO users (first_name, last_name, birthdate) 
            VALUES (:first_name, :last_name, :birthdate)
        """)
    connection.execute(
        sql,
        {"first_name": "Hi", "last_name": "Mizu", "birthdate": datetime.now()}
    )

    connection.commit()
