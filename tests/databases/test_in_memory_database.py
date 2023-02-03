"""test in memory database"""
from src.databases.in_memory_database import TodoInMemoryDatabaseService


class TodoInMemoryDatabaseTest:
    """Todo In Memory Database Tests"""

    def test_successfully_persists_todo(
        self, in_memory_database: TodoInMemoryDatabaseService
    ):
        """test saves todo"""
        todos_before_save = in_memory_database.read_all()
        len_before_save = len(todos_before_save)

        todo = in_memory_database.save_todo({"title": "Test Title", "completed": True})

        todos_after_save = in_memory_database.read_all()
        len_after_save = len(todos_after_save)

        assert len_before_save != len_after_save
        assert todo == todos_after_save[-1]

    def test_retrieves_all_todos(
        self,
        in_memory_database: TodoInMemoryDatabaseService,
        in_memory_database_empty: TodoInMemoryDatabaseService,
    ):
        """test retrieves all todos"""
        todos = in_memory_database.read_all()
        todos_empty = in_memory_database_empty.read_all()

        assert len(todos) == 5
        assert len(todos_empty) == 0
