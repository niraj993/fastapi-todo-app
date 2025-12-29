import sqlite3
from database.connectors.base import DatabaseConnector
from configs.db_configs import DATABASE_NAME


class SQLiteConnector(DatabaseConnector):

    def __init__(self, db_name: str = DATABASE_NAME)->None:
        self.__db_name = db_name


    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            self.__db_name,
            check_same_thread=False
        )   
        connection.row_factory = sqlite3.Row
        return connection
