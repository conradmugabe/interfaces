"""conftest.py"""
from typing import List

import pytest

from src.todo import Todo, CreateTodo


@pytest.fixture
def todo_list() -> List[Todo]:
    """todo list"""
    todo_one: Todo = {
        "id": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "title": "test title 1",
        "user_id": "913694c6-435a-4366-ba0d-da5334a611b2",
        "completed": False,
    }
    return [todo_one]


@pytest.fixture
def todo_data() -> CreateTodo:
    """create todo data"""
    data: CreateTodo = {
        "completed": False,
        "title": "test title 1",
        "user_id": "913694c6-435a-4366-ba0d-da5334a611b2",
    }
    return data
