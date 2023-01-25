"""todo entity"""
from typing import TypedDict
from uuid import UUID


class Todo(TypedDict):
    """Todo Entity"""

    id: UUID
    title: str
    user_id: UUID
    completed: bool