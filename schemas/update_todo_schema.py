from pydantic import BaseModel,Field
from typing import Optional
from .create_todo_schema import TodoStatus
from datetime import date



class UpdateTodoSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TodoStatus] = None