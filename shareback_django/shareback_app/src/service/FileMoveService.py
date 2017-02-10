import shutil

from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileMoveService(BaseService):

    # Accepts File Array and Move files
    def move(self, src_arr, dest_arr):
        return FileOperations(self.user_id).move(src_arr, dest_arr)