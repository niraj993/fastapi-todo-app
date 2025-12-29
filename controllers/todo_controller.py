from typing import List, Dict, Optional
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from models.todo_model import TodoModel
from schemas.create_todo_schema import CreateTodoSchema
from schemas.update_todo_schema import UpdateTodoSchema
from database.connectors.base import DatabaseConnector
from configs.response_messages import *
from configs.constants import MESSAGE,STATUS_CODE,TODO_ID,TODOS_DATA
from schemas.todo_response_schema import TodoItemResponse
from utils.db_utils import rows_to_dicts



class TodoController:

    @staticmethod
    def create_todo(create_request_payload: CreateTodoSchema, connector: DatabaseConnector) -> JSONResponse:
        try:
            todo_id = TodoModel.insert_todo(payload=create_request_payload, connector=connector)
            return JSONResponse(
                status_code=201,
                content={STATUS_CODE:201,MESSAGE: TODO_CREATED_MESSAGE, TODO_ID: todo_id}
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_MESSAGE.format(error=e))


    @staticmethod
    def fetch_todos(connector: DatabaseConnector,
                    page: int = 1,
                    page_size: int = 5) -> JSONResponse:
        try:
            rows: List[Dict] = TodoModel.get_todos_page(connector=connector,page=page,page_size=page_size)
            return JSONResponse(status_code=200, content={STATUS_CODE:200,MESSAGE:TODO_FETCHED_MESSAGE,TODOS_DATA:rows_to_dicts(rows) })
        except Exception as e:
            raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_MESSAGE.format(error=e))


    @staticmethod
    def fetch_todo_by_id(todo_id: int, connector: DatabaseConnector) -> JSONResponse:
        try:
            todo: Optional[Dict] = TodoModel.get_todo_by_id(todo_id=todo_id, connector=connector)
            if not todo:
                raise HTTPException(status_code=404, detail=TODO_NOT_FOUND_MESSAGE.format(todo_id=todo_id))
            return JSONResponse(status_code=200, content={STATUS_CODE:200,MESSAGE:TODO_FETCHED_MESSAGE,TODOS_DATA: rows_to_dicts(todo) })
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_MESSAGE.format(error=e))


    @staticmethod
    def update_todo(todo_id: int, payload: UpdateTodoSchema, connector: DatabaseConnector) -> JSONResponse:
        try:
            todo: Optional[Dict] = TodoModel.get_todo_by_id(todo_id=todo_id, connector=connector)
            if not todo:
                raise HTTPException(status_code=404, detail=TODO_NOT_FOUND_MESSAGE.format(todo_id=todo_id))
            updated_rows = TodoModel.update_todo(todo_id=todo_id, payload=payload, connector=connector)
            if updated_rows:
                raise HTTPException(status_code=404, detail=TODO_NOT_FOUND_MESSAGE.format(todo_id=todo_id))
            return JSONResponse(status_code=200, content={STATUS_CODE:200,MESSAGE: TODO_UPDATED_MESSAGE})
        except HTTPException:
            raise
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_MESSAGE.format(error=e))


    @staticmethod
    def delete_todo(todo_id: int, connector: DatabaseConnector) -> JSONResponse:
        try:
            deleted_rows = TodoModel.delete_todo(todo_id=todo_id, connector=connector)
            if deleted_rows == 0:
                raise HTTPException(status_code=404, detail=TODO_NOT_FOUND_MESSAGE.format(todo_id=todo_id))
            return JSONResponse(status_code=200, content={STATUS_CODE:200,MESSAGE: TODO_DELETED_MESSAGE})
        except Exception as e:
            raise HTTPException(status_code=500, detail=INTERNAL_SERVER_ERROR_MESSAGE.format(error=e))
