"""test in memory database"""
from typing import List

from src.databases.mongo_database import TodoMongoDatabaseService


class TodoMongoDatabaseServiceTest:
    """Todo In Memory Database Tests"""

    def test_successfully_persists_todo(
        self, mongo_database_config: str, mongo_database: TodoMongoDatabaseService
    ):
        """test saves todo"""
        database = TodoMongoDatabaseService(mongo_database_config)
        todos_before_save = database.read_all()
        len_before_save = len(todos_before_save)

        todo = database.save_todo({"title": "Test Title", "completed": True})

        todos_after_save = database.read_all()
        len_after_save = len(todos_after_save)

        assert len_before_save != len_after_save
        assert todo == todos_after_save[-1]

    def test_retrieves_all_todos(
        self, mongo_database_config: str, mongo_database: TodoMongoDatabaseService, create_todo_list: List[CreateTodo] 
    ):
        """test retrieves all todos"""
        database = TodoMongoDatabaseService(mongo_database_config)
        todos = database.read_all()

        assert len(todos) == len(create_todo_list)
