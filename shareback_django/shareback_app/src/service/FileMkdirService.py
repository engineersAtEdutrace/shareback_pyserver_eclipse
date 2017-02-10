from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileMkdirService(BaseService):

    # Accepts Directory Array and Create Directories
    def mkdir(self, dir_arr):
        return FileOperations(self.user_id).mkdir(dir_arr)