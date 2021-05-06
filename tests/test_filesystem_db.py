from src.filesystem_db import FileSystemDb


class Test_FileSystemDb:
    def test_fileExists(self):
        # prepare
        file_one = "no_file"
        file_two = "test_file"
        content_one = "test_content"

        # assert
        fs = FileSystemDb.getInstance(re_init=True)
        notFileExists = fs._fileExists(file_one)

        fs.create(file_two, content_one)
        fileExists = fs._fileExists("test_file")

        # assert
        assert notFileExists == f"file {file_one} does not exist"
        assert fileExists is None

    def test_readAll(self):
        # prepare
        file_one = "file_one"
        content_one = "content_one"
        file_two = "file_two"
        content_two = "content_two"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        fs.create(file_one, content_one)
        fs.create(file_two, content_two)

        # assert
        assert fs.readAll() == [file_one, file_two]

    def test_create(self):
        # prepare
        test_file = "test_file"
        test_content = "test_content"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        created = fs.create(test_file, test_content)

        # assert
        assert created == {test_file: test_content}

    def test_update(self):
        # prepare
        file = "test_file"
        content = "test_content"
        updated_content = "updated_contents"

        no_file = "no_file"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        fs.create(file, content)
        updated_file = fs.update(file, updated_content)

        file_not_updated = fs.update(no_file, content)

        # assert
        assert updated_file == {file: updated_content}
        assert file_not_updated == f"file {no_file} does not exist"

    def test_read(self):
        # prepare
        file = "test_file"
        content = "test_content"

        no_file = "no_file"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        fs.create(file, content)
        readFile = fs.read(file)

        noReadFile = fs.read(no_file)

        # assert
        assert readFile == content
        assert noReadFile == f"file {no_file} does not exist"

    def test_delete(self):
        # prepare
        file = "test_file"
        content = "test_content"
        no_file = "no_file"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        fs.create(file, content)
        readFile = fs.delete(file)

        noReadFile = fs.delete(no_file)

        # assert
        assert readFile == file
        assert noReadFile == f"file {no_file} does not exist"

    def test_deleteFileContents(self):
        # prepare
        file = "test_content"
        content = "test_content"
        no_file = "no_file"

        # test
        fs = FileSystemDb.getInstance(re_init=True)
        fs.create(file, content)
        deleted_file = fs.deleteFileContents(file)

        no_deleted_file = fs.deleteFileContents(no_file)

        # assert
        assert deleted_file == {file: None}
        assert no_deleted_file == f"file {no_file} does not exist"
