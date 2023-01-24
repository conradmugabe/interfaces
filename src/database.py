"""todo database service module"""
from abc import ABC, abstractmethod


class TodoDataBaseService(ABC):
    """Todo Database Service"""

    @abstractmethod
    def save_todo(self):
        """saves todo to database"""

    @abstractmethod
    def read_all(self):
        """retrieve todos in database"""

    @abstractmethod
    def read_by_id(self, id: str):
        """retrieve a todo from the database"""

    @abstractmethod
    def update(self, id: str):
        """update a todo in the database"""

    @abstractmethod
    def delete(self, id: str):
        """delete a todo from the database"""
