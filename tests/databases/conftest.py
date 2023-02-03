"""conftest database"""
from uuid import uuid4
from typing import List

import pytest

from src.entities.todo import CreateTodo, Todo
from src.databases.in_memory_database import TodoInMemoryDatabaseService


@pytest.fixture
def create_todo_list() -> List[CreateTodo]:
    """create todo list"""
    return [
        {
            "title": "quis ut nam facilis et officia qui",
            "completed": False,
        },
        {
            "title": "fugiat veniam minus",
            "completed": True,
        },
        {
            "title": "et porro tempora",
            "completed": True,
        },
        {
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False,
        },
        {
            "title": "qui ullam ratione quibusdam voluptatem quia omnis",
            "completed": False,
        },
    ]


@pytest.fixture
def todo_list(create_todo_list: List[CreateTodo]) -> List[Todo]:
    """todo list"""
    todos: List[Todo] = []
    for item in create_todo_list:
        todos.append({**item, "id": uuid4()})
    return todos


@pytest.fixture
def in_memory_database(todo_list: List[Todo]) -> TodoInMemoryDatabaseService:
    """in memory database"""
    database = TodoInMemoryDatabaseService(todo_list)
    return database


@pytest.fixture
def in_memory_database_empty() -> TodoInMemoryDatabaseService:
    """empty in memory database"""
    database = TodoInMemoryDatabaseService()
    return database
