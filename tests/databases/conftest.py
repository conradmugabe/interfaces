"""conftest database"""
from uuid import uuid4
from typing import List

import pytest
import sqlalchemy
from pymongo import MongoClient
from sqlalchemy.orm import sessionmaker

from src.entities.todo import CreateTodo, Todo
from src.databases.model.todo import Base, TodoModel
from src.databases.mongo_database import TodoMongoDatabaseService
from src.databases.in_memory_database import TodoInMemoryDatabaseService
from src.databases.postgres_database import TodoPostgresDatabaseService


@pytest.fixture(scope="session")
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
def create_todo_array() -> List[CreateTodo]:
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
def todo_list(create_todo_array: List[CreateTodo]) -> List[Todo]:
    """todo list"""
    todos: List[Todo] = []
    for item in create_todo_array:
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


@pytest.fixture(scope="session")
def mongo_database_config() -> str:
    """mongo database config"""
    return "mongodb://localhost:27017/"


@pytest.fixture(scope="session")
def mongo_database_empty(mongo_database_config: str):
    """create empty mongo database"""
    client = MongoClient(mongo_database_config)
    database = client["test"]

    yield database

    client.drop_database("test")
    client.close()


@pytest.fixture(scope="function")
def mongo_database(
    mongo_database_empty: TodoMongoDatabaseService, create_todo_list: List[CreateTodo]
):
    """populate mongo database"""
    collection = mongo_database_empty["todos"]
    collection.insert_many(create_todo_list)

    yield mongo_database_empty

    collection.delete_many({})


@pytest.fixture(scope="session")
def postgres_database_config() -> str:
    """postgres database config"""
    return "postgresql://user:testing@localhost:5432/"


@pytest.fixture(scope="session")
def postgres_database_empty(postgres_database_config: str):
    """start instance of empty postgres db"""
    engine = sqlalchemy.create_engine(postgres_database_config)
    connection = engine.connect()

    Base.metadata.create_all(bind=engine)
    DatabaseSession = sessionmaker(bind=engine)
    session = DatabaseSession()

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope="function")
def postgres_database(postgres_database_empty: TodoPostgresDatabaseService, create_todo_list: List[CreateTodo]):
    """populate postgres database"""
    for todo in create_todo_list:
        postgres_database_empty.add(
            TodoModel(title=todo["title"], completed=todo["completed"])
        )
        postgres_database_empty.commit()

    yield postgres_database_empty

    postgres_database_empty.query(TodoModel).delete()
