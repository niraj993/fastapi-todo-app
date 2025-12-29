from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from database.connectors.base import DatabaseConnector
from dependencies import get_sqlite_db_connection
from schemas.create_todo_schema import CreateTodoSchema
from schemas.update_todo_schema import UpdateTodoSchema
from controllers.todo_controller import TodoController
from configs.constants import TODO_TAG
from configs.endpoints import TODOS_ENDPOINT, TODO_BY_ID_ENDPOINT
from schemas.todo_response_schema import TodoListResponse

router: APIRouter = APIRouter(tags=[TODO_TAG])


@router.post(path=TODOS_ENDPOINT, response_model=TodoListResponse)
def add_todo_item(
    request: Request,
    create_request_payload: CreateTodoSchema,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> JSONResponse:
    return TodoController.create_todo(create_request_payload=create_request_payload, connector=connector)



@router.get(path=TODOS_ENDPOINT, response_model=TodoListResponse)
def get_all_todos(
    page: int = 1,
    page_size: int = 5,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> JSONResponse:
    return TodoController.fetch_todos(connector=connector,page=page,page_size=page_size)



@router.get(path=TODO_BY_ID_ENDPOINT, response_model=TodoListResponse)
def get_todo_by_id(
    todo_id: int,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> JSONResponse:
    return TodoController.fetch_todo_by_id(todo_id=todo_id, connector=connector)



@router.put(path=TODO_BY_ID_ENDPOINT, response_model=TodoListResponse)
def update_todo(
    todo_id: int,
    payload: UpdateTodoSchema,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> JSONResponse:
    return TodoController.update_todo(todo_id=todo_id, payload=payload, connector=connector)



@router.delete(path=TODO_BY_ID_ENDPOINT, response_model=TodoListResponse)
def delete_todo(
    todo_id: int,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> JSONResponse:
    return TodoController.delete_todo(todo_id=todo_id, connector=connector)
