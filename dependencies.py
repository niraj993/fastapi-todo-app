from database.connectors.sqlite import SQLiteConnector
from database.connectors.base import DatabaseConnector


def get_sqlite_db_connection()->DatabaseConnector:
    return SQLiteConnector()


def get_postgres_db_connection()->DatabaseConnector:
    return 


