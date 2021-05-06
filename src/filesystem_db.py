from typing import Any
instance = None


class FileSystemDb:

    def _fileExists(self, file_name: str) -> Any:
        """
        checks if file in file system

        Args:
            `file_name (str)` file name in file system

        Returns:
            `None` if file exists else `str`
        """
        if self.files.get(file_name) is None:
            return "file {} does not exist".format(file_name)
        return None

    def readAll(self) -> list:
        """
        read all contents in the filesystem

        Returns:
            `file_names (list)` all files in file system
        """
        file_names = list()
        for file in self.files:
            file_names.append(file)
        return file_names

    def create(self, file_name: str, data: Any) -> dict:
        """
        create and a file and its contents

        Args:
            `file_name (obj)` file name to be created
            `data (Any)` content to be saved in side file

        Returns:
            `dict` file and contents of the file
        """
        self.files[file_name] = data
        return {file_name: data}

    def update(self, file_name: str, data: Any) -> Any:
        """
        update and existing file's contents

        Args:
            `file_name (str)` file to be created;
            `data (Any)` data to be store in file

        Returns:
            `dict` if successful else `None`
        """
        reason = self._fileExists(file_name)

        if reason is None:
            return self.create(file_name, data)

        return reason

    def read(self, file_name: str):
        """
        read contents of a file

        Args:
            `file_name (str)` file name to be deleted

        Returns:
            `dict` if successful else `None`     
        """
        reason = self._fileExists(file_name)

        if reason is None:
            return self.files[file_name]

        return reason

    def delete(self, file_name: str):
        """
        delete file from file system

        Args:
            `file_name (str)` file name to be deleted

        Returns:
            `str` file name if successful else `None`
        """
        reason = self._fileExists(file_name)

        if reason is None:
            self.files.pop(file_name)
            return file_name

        return reason

    def deleteFileContents(self, file_name: str) -> Any:
        """
        delete contents of an existing file

        Args:
            `file_name (str)` file name of contents to be deleted

        Returns:
            `dict` if deletion successful else `None`
        """
        reason = self._fileExists(file_name)

        if reason is None:
            self.files[file_name] = None
            return {file_name: None}

        return reason

    def __init__(self) -> None:
        self.files = dict()

    @staticmethod
    def getInstance(re_init=False):
        """ge an instance of FileSystemDb"""
        global instance
        if instance is None or re_init is True:
            return FileSystemDb()
        return instance
