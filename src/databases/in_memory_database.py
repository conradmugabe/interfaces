"""in memory database service"""
from uuid import uuid4
from typing import List

from src.entities.todo import Todo, CreateTodo
from src.databases.database import TodoDataBaseService


class TodoInMemoryDatabaseService(TodoDataBaseService):
    """In Memory Database Service"""

    def __init__(self, data: List[Todo] = None) -> None:
        if data is None:
            data = []
        self._data = data

    def save_todo(self, data: CreateTodo):
        """saves todo"""
        todo: Todo = {**data, "id": uuid4()}
        self._data.append(todo)
        return todo

    def read_all(self) -> List[Todo]:
        """retrieves todos"""
        return self._data
