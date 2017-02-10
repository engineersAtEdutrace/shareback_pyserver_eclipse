from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileCopyService(BaseService):

    # Accepts list of files and paste to destination path
    def copy(self, file_arr, destination_path):
        operation = FileOperations(self.user_id)
        return operation.copy(file_arr, destination_path)