from abc import ABCMeta, abstractmethod

from shareback_app.src.util.FilePathConverter import FilePathConverter


class BaseAdapter:

    def __init__(self, request):
        self.request = request
        self.user_id = 'NOT INITIALIZED'
        self.path_converter = FilePathConverter(self.user_id)

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
