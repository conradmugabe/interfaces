"""todo database service"""
from abc import ABC, abstractmethod
from typing import List

from src.todo import Todo, CreateTodo


class TodoDataBaseService(ABC):
    """Todo Database Service"""

    @abstractmethod
    def save_todo(self, data: CreateTodo) -> Todo:
        """saves todo"""

    @abstractmethod
    def read_all(self) -> List[Todo]:
        """retrieves todos"""
