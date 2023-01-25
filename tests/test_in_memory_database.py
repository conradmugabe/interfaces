"""in memory database service test"""
from typing import List

from src.todo import Todo, CreateTodo
from src.in_memory_database import TodoInMemoryDatabaseService


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

    def test_successfully_instantiates_with_todo_array(self, todo_list: List[Todo]):
        """database instances"""
        database = TodoInMemoryDatabaseService.get_instance(
            data=todo_list, re_init=True
        )
        assert database.read_all() == todo_list
        assert len(database.read_all()) == 1

    def test_successfully_saves_todo(self, todo_data: CreateTodo):
        """successfully saves data to database"""

        database = TodoInMemoryDatabaseService.get_instance(re_init=True)
        todo = database.save_todo(todo_data)

        assert todo["completed"] == todo_data["completed"]
        assert todo["title"] == todo_data["title"]
        assert todo["user_id"] == todo_data["user_id"]
        assert database.read_all() == [todo]
        assert len(database.read_all()) == 1

    def test_returns_todo_if_found_in_database(self, todo_list: List[Todo]):
        """returns todo if in database"""
        database = TodoInMemoryDatabaseService.get_instance(
            data=todo_list, re_init=True
        )
        todo_id = todo_list[0]["id"]
        todo = database.read_by_id(todo_id=todo_id)

        assert todo == todo_list[0]

    def test_returns_none_if_todo_not_found(self):
        """returns None if todo not found"""
        database = TodoInMemoryDatabaseService.get_instance(re_init=True)

        todo = database.read_by_id(todo_id="123213")

        assert todo is None

    def test_successfully_deletes_todo(self, todo_list: List[Todo]):
        """successfully deletes todo from database, given an id"""
        database = TodoInMemoryDatabaseService.get_instance(
            data=todo_list, re_init=True
        )

        assert len(database.read_all()) == 1

        database.delete("fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a")

        assert len(database.read_all()) == 0

    def test_successfully_updates_todo(self, todo_list: List[Todo]):
        """successfully updates todo"""
        database = TodoInMemoryDatabaseService.get_instance(
            data=todo_list, re_init=True
        )
        todo_id = todo_list[0]["id"]
        todo_before_update = database.read_by_id(todo_id=todo_id)

        todo: Todo = {**todo_before_update, "completed": True}

        todo_after_update = database.update(todo=todo)

        assert not todo_before_update["completed"]
        assert todo_after_update["completed"]
        assert todo_before_update["completed"] != todo_after_update["completed"]
        assert todo_before_update["id"] == todo_after_update["id"]
        assert todo_before_update["user_id"] == todo_after_update["user_id"]
        assert todo_before_update["title"] == todo_after_update["title"]

    def test_returns_none_if_no_update_occurred(self, todo_list: List[Todo]):
        """returns none if no update occurs"""
        database = TodoInMemoryDatabaseService.get_instance(re_init=True)

        todo = todo_list[0]
        updated_todo = database.update(todo=todo)

        assert updated_todo is None
