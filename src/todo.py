"""todo entity"""
from uuid import UUID
from typing import TypedDict


class Todo(TypedDict):
    """Todo Entity"""

    id: UUID
    title: str
    user_id: UUID
    completed: bool


class CreateTodo(TypedDict):
    """Create Todo"""

    title: str
    user_id: UUID
    completed: bool
