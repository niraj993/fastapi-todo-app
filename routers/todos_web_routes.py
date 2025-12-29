from pathlib import Path
from typing import List, Optional
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from configs.constants import TODO_WEB_TAG
from database.connectors.base import DatabaseConnector
from dependencies import get_sqlite_db_connection
from models.todo_model import TodoModel
from schemas.create_todo_schema import CreateTodoSchema, TodoStatus
from schemas.update_todo_schema import UpdateTodoSchema
from configs.constants import TEMPLATES

BASE_DIR = Path(__file__).resolve().parent.parent

router:APIRouter = APIRouter(tags=[TODO_WEB_TAG])
templates = Jinja2Templates(directory=str(BASE_DIR / TEMPLATES))



@router.get("/", response_class=HTMLResponse)
def list_todos(
    request: Request,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> HTMLResponse:
    todos: List[dict] = TodoModel.get_todos(connector=connector)
    return templates.TemplateResponse(
        "todos_list.html",
        {"request": request, "todos": todos}
    )



@router.get("/todos", response_class=HTMLResponse)
def create_todo_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "todo_create.html",
        {"request": request}
    )



@router.post("/todos", response_class=RedirectResponse)
def create_todo_web(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    due_date: Optional[str] = Form(None),
    status: TodoStatus = Form(TodoStatus.pending),
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> RedirectResponse:
    payload = CreateTodoSchema(
        title=title,
        description=description,
        due_date=due_date,
        status=status
    )
    TodoModel.insert_todo(payload=payload, connector=connector)
    return RedirectResponse(url="/", status_code=303)



@router.get("/todos/{todo_id}/edit", response_class=HTMLResponse)
def edit_todo_page(
    todo_id: int,
    request: Request,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> HTMLResponse:
    todo: dict = TodoModel.get_todo_by_id(todo_id=todo_id, connector=connector)
    return templates.TemplateResponse(
        "todo_update.html",
        {"request": request, "todo": todo}
    )



@router.post("/todos/{todo_id}/edit", response_class=RedirectResponse)
def update_todo_web(
    todo_id: int,
    title: str = Form(...),
    description: Optional[str] = Form(None),
    due_date: Optional[str] = Form(None),
    status: TodoStatus = Form(...),
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> RedirectResponse:
    payload = UpdateTodoSchema(
        title=title,
        description=description,
        due_date=due_date,
        status=status
    )
    TodoModel.update_todo(todo_id=todo_id, payload=payload, connector=connector)
    return RedirectResponse(url="/", status_code=303)



@router.post("/todos/{todo_id}/delete", response_class=RedirectResponse)
def delete_todo_web(
    todo_id: int,
    connector: DatabaseConnector = Depends(get_sqlite_db_connection)
) -> RedirectResponse:
    TodoModel.delete_todo(todo_id=todo_id, connector=connector)
    return RedirectResponse(url="/", status_code=303)
