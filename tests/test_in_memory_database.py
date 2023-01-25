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
        todo_one: Todo = {
            "id": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "title": "test title 1",
            "user_id": "913694c6-435a-4366-ba0d-da5334a611b2",
            "completed": False,
        }
        data = [todo_one]
        database = TodoInMemoryDatabaseService.get_instance(data=data, re_init=True)

        assert len(database.read_all()) == 1
        assert database.read_all() == data