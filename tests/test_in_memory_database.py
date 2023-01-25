from src.in_memory_database import TodoInMemoryDatabaseService
from src.todo import Todo


class TodoInMemoryDatabaseServiceTest:
    """TodoInMemoryDatabaseService Test class"""

    def test_uses_same_instance_of_the_database(self):
        """database instances"""
        instance_one = TodoInMemoryDatabaseService.get_instance()
        instance_two = TodoInMemoryDatabaseService.get_instance()

        assert instance_one == instance_two

    def test_uses_different_instances_of_the_database(self):
        """database instances"""
        instance_one = TodoInMemoryDatabaseService.get_instance(re_init=True)
        instance_two = TodoInMemoryDatabaseService.get_instance(re_init=True)

        assert instance_one != instance_two

    def test_successfully_instantiates_with_todo_array(self):
        """database instances"""
        todo_one: Todo = dict({"id", "", "title": "todo 1", "user_id": "", "completed": False})
        todo_two: Todo = dict({"id", "", "title": "todo 2", "user_id": "", "completed": True})
        database = TodoInMemoryDatabaseService.get_instance(data=[todo_one, todo_two])

        assert len(database._data) == 2