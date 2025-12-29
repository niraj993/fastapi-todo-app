from database.connectors.base import DatabaseConnector
from configs.sql_queries import CREATE_TODOS_TABLE_SQL_QUERY


class DatabaseInitializer:
    """
    Initializes database schema.
    """

    def __init__(self, connector: DatabaseConnector):
        self.__connector = connector


    def initialize_schema(self) -> None:
        with self.__connector.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(CREATE_TODOS_TABLE_SQL_QUERY)
            connection.commit()



