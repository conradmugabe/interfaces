"""todo database service"""
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.entities.todo import Todo, CreateTodo
from src.databases.database import TodoDataBaseService
from src.databases.model.todo import Base, TodoModel


class TodoPostgresDatabaseService(TodoDataBaseService):
    """Todo Database Service"""

    def __init__(self, uri: str) -> None:
        """initialize database"""
        self._engine = create_engine(uri)
        Base.metadata.create_all(bind=self._engine)

    def _session(self):
        """get instance of session"""
        DatabaseSession = sessionmaker(bind=self._engine)
        return DatabaseSession()

    def _create_todo_object(self, result):
        return {
            "id": result.id,
            "title": result.title,
            "completed": result.completed,
        }

    def save_todo(self, data: CreateTodo) -> Todo:
        """saves todo"""
        session = self._session()

        todo = TodoModel(title=data["title"], completed=data["completed"])
        session.add(todo)
        session.commit()
        return self._create_todo_object(todo)

    def read_all(self) -> List[Todo]:
        """retrieves todos"""
        session = self._session()

        results = session.query(TodoModel).all()
        return [self._create_todo_object(result) for result in results]
