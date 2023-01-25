class TodoInMemoryDatabaseService:

    _instance = None

    @staticmethod
    def get_instance(re_init=False):
        """get an instance of TodoInMemoryDatabaseService"""
        
        if TodoInMemoryDatabaseService._instance is None or re_init is True:
            TodoInMemoryDatabaseService._instance = TodoInMemoryDatabaseService()
        return TodoInMemoryDatabaseService._instance
