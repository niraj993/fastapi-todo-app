from typing import List, Optional, Dict
from schemas.create_todo_schema import CreateTodoSchema
from schemas.update_todo_schema import UpdateTodoSchema
from database.connectors.base import DatabaseConnector
from configs.sql_queries import *


class TodoModel:

    @staticmethod
    def insert_todo(payload: CreateTodoSchema, connector: DatabaseConnector) -> int:
        """
        Inserts a new todo into the database.
        Returns the ID of the newly created todo.
        """
        return connector.execute(
            CREATE_TODOS_SQL_QUERY,
            (
                payload.title,
                payload.description,
                payload.due_date,
                payload.status,
            ),
            commit=True
        ).lastrowid

  
    @staticmethod
    def get_todos_page(
        connector: DatabaseConnector,
        page: int = 1,
        page_size: int = 5
    ) -> List[Dict]:
        if page < 1:
            page = 1

        if page_size < 1:
            page_size = 5
        offset = (page - 1) * page_size
        paginated_query = f"""
            {GET_ALL_TODOS_SQL_QUERY}
            LIMIT ? OFFSET ?
        """
        return connector.execute(
            paginated_query,
            (page_size, offset),
            fetchall=True
        )
    

    def get_todos(connector: DatabaseConnector) -> List[Dict]: 
        """ Retrieves all todos from the database. 
        Returns a list of dictionaries representing todos. """ 
        return connector.execute(query=GET_ALL_TODOS_SQL_QUERY, fetchall=True)

    @staticmethod
    def get_todo_by_id(todo_id: int, connector: DatabaseConnector) -> Optional[Dict]:
        """
        Retrieves a single todo by ID.
        Returns a dictionary representing the todo or None if not found.
        """
        return connector.execute(
            GET_TODO_BY_ID_SQL_QUERY,
            (todo_id,),
            fetchone=True
        )

    @staticmethod
    def update_todo(
        todo_id: int,
        payload: UpdateTodoSchema,
        connector: DatabaseConnector
    ) -> int:
        """
        Updates a todo by ID.
        Returns the number of rows updated (0 if not found).
        """
        return connector.execute(
            UPDATE_TODO_SQL_QUERY,
            (
                payload.title,
                payload.description,
                payload.due_date,
                payload.status,
                todo_id,
            ),
            commit=True
        ).rowcount


    @staticmethod
    def delete_todo(todo_id: int, connector: DatabaseConnector) -> int:
        """
        Deletes a todo by ID.
        Returns the number of rows deleted (0 if not found).
        """
        return connector.execute(
            DELETE_TODO_SQL_QUERY,
            (todo_id,),
            commit=True
        ).rowcount
