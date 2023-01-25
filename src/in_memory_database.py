"""in memory database service"""
from typing import List
from uuid import uuid4

from src.todo import Todo, CreateTodo
from src.database import TodoDataBaseService


class TodoInMemoryDatabaseService(TodoDataBaseService):
    """In Memory Database Service"""

    _instance = None

    def __init__(self, data: List[Todo] = None) -> None:
        if data is None:
            data = []
        self._data = data

    def save_todo(self, data: CreateTodo):
        """saves todo to database"""
        todo: Todo = {"id": uuid4(), **data}
        self._data.append(todo)
        return todo

    def read_all(self) -> List[Todo]:
        """retrieve todos from database"""
        return self._data

    def read_by_id(self, todo_id: str):
        """retrieve a todo from the database"""
        for todo in self._data:
            if todo["id"] == todo_id:
                return todo
        return None

    def update(self, todo: Todo):
        """update a todo in the database"""
        for index, value in enumerate(self._data):
            if value["id"] == todo["id"]:
                self._data[index] = {**value, **todo}
                return self._data[index]
        return None

    def delete(self, todo_id: str):
        """delete a todo from the database"""
        for index, value in enumerate(self._data):
            if value["id"] == todo_id:
                self._data = self._data[:index] + self._data[index + 1 :]
                return value
        return None

    @staticmethod
    def get_instance(data: List[Todo] = None, re_init=False):
        """get an instance of TodoInMemoryDatabaseService"""
        if TodoInMemoryDatabaseService._instance is None or re_init is True:
            TodoInMemoryDatabaseService._instance = TodoInMemoryDatabaseService(
                data=data
            )
        return TodoInMemoryDatabaseService._instance
