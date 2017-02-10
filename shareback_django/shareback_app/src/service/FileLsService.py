from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileLsService(BaseService):

    # Accepts Directory array and returns List< Dir_Array[], File_Array[] >
    def ls(self, dir):
        return FileOperations(self.user_id).ls(dir)
