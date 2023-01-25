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