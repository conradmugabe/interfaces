"""todo entity"""
from uuid import UUID
from typing import TypedDict


class CreateTodo(TypedDict):
    """Create Todo Dto"""
    title: str
    completed: bool

class Todo(CreateTodo):
    """Todo Entity"""

    id: UUID