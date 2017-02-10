from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileDeleteService(BaseService):

    # Accepts file array and remove files
    def delete(self, file_arr):
        return FileOperations(self.user_id).delete(file_arr)