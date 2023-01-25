from typing import List

from src.todo import Todo


class TodoInMemoryDatabaseService:
    """In Memory Database Service"""

    _instance = None

    def __init__(self, data: List[Todo] = None) -> None:
        self._data = data or []

    @staticmethod
    def get_instance(data: List[Todo] = None, re_init=False):
        """get an instance of TodoInMemoryDatabaseService"""
        if TodoInMemoryDatabaseService._instance is None or re_init is True:
            TodoInMemoryDatabaseService._instance = TodoInMemoryDatabaseService()
        return TodoInMemoryDatabaseService._instance
