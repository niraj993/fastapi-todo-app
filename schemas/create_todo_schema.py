from enum import Enum
from datetime import datetime,date
from pydantic import BaseModel,Field
from typing import Optional


class TodoStatus(str,Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"




class CreateTodoSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TodoStatus = TodoStatus.pending




