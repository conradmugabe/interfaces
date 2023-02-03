"""test in memory database"""
from src.databases.postgres_database import TodoPostgresDatabaseService


class TodoPostgresDatabaseServiceTest:
    """Todo In Memory Database Tests"""

    def test_successfully_persists_todo(
        self, postgres_database_config: str, postgres_database: TodoPostgresDatabaseService
    ):
        """test saves todo"""
        database = TodoPostgresDatabaseService(postgres_database_config)
        todos_before_save = database.read_all()
        len_before_save = len(todos_before_save)

        todo = database.save_todo({"title": "Test Title", "completed": True})

        todos_after_save = database.read_all()
        len_after_save = len(todos_after_save)

        assert len_before_save != len_after_save
        assert todo == todos_after_save[-1]

    def test_retrieves_all_todos(
        self, postgres_database_config: str, postgres_database: TodoPostgresDatabaseService
    ):
        """test retrieves all todos"""
        database = TodoPostgresDatabaseService(postgres_database_config)
        todos = database.read_all()

        assert len(todos) == 5
