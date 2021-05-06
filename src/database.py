instance = None


class DataBase:

    def __init__(self, provider) -> None:
        self.provider = provider

    def create(self, file_name, data):
        return self.provider.create(file_name, data)

    def readAll(self):
        return self.provider.readAll()

    def read(self, file_name):
        return self.provider.read(file_name)

    def update(self, file_name, data):
        return self.provider.update(file_name, data)

    def delete(self, file_name):
        return self.provider.delete(file_name)

    @staticmethod
    def getInstance(provider=None, re_init=False):
        global instance
        if instance is None or re_init is True:
            return DataBase(provider)
        return instance
