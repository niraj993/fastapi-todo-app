from pydantic import BaseModel
from typing import List, Optional, Dict

class TodoItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[str]
    status: str
    created_at: Optional[str]
    updated_at: Optional[str]



class TodoListResponse(BaseModel):
    todos: List[TodoItemResponse]
