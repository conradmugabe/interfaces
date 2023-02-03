"""mongo database service"""
from typing import List

from pymongo import MongoClient

from src.entities.todo import Todo, CreateTodo
from src.databases.database import TodoDataBaseService


class TodoMongoDatabaseService(TodoDataBaseService):
    """Mongo Database Service"""

    def __init__(self, uri: str) -> None:
        self._client = MongoClient(uri)
        self._database = self._client["test"]

    def _todo_collection(self):
        """gets todo collection"""
        return self._database["todos"]

    def _create_todo_object(self, result):
        """create todo object"""
        return {
            "id": str(result["_id"]),
            "title": result["title"],
            "completed": result["completed"],
        }

    def save_todo(self, data: CreateTodo) -> Todo:
        """saves todo"""
        collection = self._todo_collection()
        todo = collection.insert_one(data)
        result = collection.find_one(todo.inserted_id)
        return self._create_todo_object(result)

    def read_all(self) -> List[Todo]:
        """retrieves todos"""
        collection = self._todo_collection()
        results = collection.find()
        return [self._create_todo_object(result) for result in results]
