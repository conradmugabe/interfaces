"""test in memory database"""
from src.databases.postgres_database import TodoPostgresDatabaseService


class TodoPostgresDatabaseServiceTest:
    """Todo In Memory Database Tests"""

    def test_successfully_persists_todo(self):
        """test saves todo"""

    def test_retrieves_all_todos(
        self, postgres_database_config: str, postgres_database: TodoPostgresDatabaseService
    ):
        """test retrieves all todos"""
        database = TodoPostgresDatabaseService(postgres_database_config)
        todos = database.read_all()

        assert len(todos) == 5
