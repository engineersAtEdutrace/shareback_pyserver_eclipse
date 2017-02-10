from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.FileOperations import FileOperations


class FileUploadService(BaseService):

    # Accepts List of File Paths and List of New Names
    # Sample Input ['/user/sagar/old_file.txt'], ['new_file.txt]
    def upload(self, file_dir, file):
        return FileOperations(self.user_id).upload(file_dir, file)