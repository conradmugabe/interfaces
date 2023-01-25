"""in memory database service"""
from typing import List

from src.todo import Todo
from src.database import TodoDataBaseService


class TodoInMemoryDatabaseService(TodoDataBaseService):
    """In Memory Database Service"""

    _instance = None

    def __init__(self, data: List[Todo] = None) -> None:
        if data is None:
            data = []
        self._data = data

    def save_todo(self):
        """saves todo to database"""

    def read_all(self) -> List[Todo]:
        """retrieve todos from database"""
        return self._data

    def read_by_id(self, todo_id: str):
        """retrieve a todo from the database"""

    def update(self, todo_id: str):
        """update a todo in the database"""

    def delete(self, todo_id: str):
        """delete a todo from the database"""

    @staticmethod
    def get_instance(data: List[Todo] = None, re_init=False):
        """get an instance of TodoInMemoryDatabaseService"""
        if TodoInMemoryDatabaseService._instance is None or re_init is True:
            TodoInMemoryDatabaseService._instance = TodoInMemoryDatabaseService(
                data=data
            )
        return TodoInMemoryDatabaseService._instance
