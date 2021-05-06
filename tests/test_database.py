from src.database import DataBase
from src.filesystem_db import FileSystemDb


class Test_DataBase:

    def test_create(self):
        # prepare
        file = "test_file"
        content = "test_content"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        db = DataBase.getInstance(provider=fs, re_init=True)

        createdFile = db.create(file, content)

        # assert
        assert createdFile == {file: content}

    def test_readAll(self):
        # prepare
        file_one = "test_file_one"
        file_two = "test_file_two"
        content_one = "test_content_one"
        content_two = "test_content_two"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        db = DataBase.getInstance(provider=fs, re_init=True)

        db.create(file_one, content_one)
        db.create(file_two, content_two)
        allFiles = db.readAll()

        # assert
        assert allFiles == [file_one, file_two]

    def test_read(self):
        # prepare
        file = "test_file"
        content = "content"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        db = DataBase.getInstance(provider=fs, re_init=True)

        db.create(file, content)
        readFile = db.read(file)

        # assert
        assert readFile == content

    def test_update(self):
        # prepare
        file = "test_file"
        content = "test_content"
        updated_content = "updated_test_content"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        db = DataBase.getInstance(provider=fs, re_init=True)

        db.create(file, content)
        updatedFile = db.update(file, updated_content)

        # assert
        assert updatedFile == {file: updated_content}

    def test_delete(self):
        # prepare
        file = "test_file"
        content = "test_content"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        db = DataBase.getInstance(provider=fs, re_init=True)

        db.create(file, content)
        deletedFile = db.delete(file)

        # assert
        assert deletedFile == file
