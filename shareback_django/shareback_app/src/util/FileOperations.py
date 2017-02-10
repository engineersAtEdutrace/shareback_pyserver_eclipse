from os.path import join, isdir, dirname
import shutil,os

from django.core.files.storage import FileSystemStorage

from shareback_app.src.Constants import Constants
from shareback_app.src.exception.InputFormatException import InputFormatException


class FileOperations:

    def __init__(self, user_id):
        self.user_id = user_id

    # Accepts file array and copies in a particular path
    def copy(self, file_arr, destination_path):
        for src_path in file_arr:
            shutil.copy2(src_path, destination_path)
        return True

    # Accepts file array and remove files
    def delete(self, file_arr):
        for file_name in file_arr:
            os.remove(file_name)
        return True

    # Accepts Directory array and returns List< List< Dir_Array[], File_Array[]> >
    def ls(self, dir):

        # Type Checking
#         if isinstance(dir_arr, basestring):
#             raise InputFormatException("Tupples or List")

        result = list()
    
        file_arr = list()
        dir_arr = list()
        obj_dict = dict()
        for f in os.listdir(dir):
            print(f)
            if isdir(join(dir, f)):
                dir_arr.append(f)
            else:
                file_arr.append(f)

        obj_dict[Constants.DIR_NAME_ARRAY] = dir_arr
        obj_dict[Constants.FILE_NAME_ARRAY] = file_arr
        result.append(obj_dict)
        return result

    # Accepts Directory Array and Create Directories
    def mkdir(self, dir):
        if not os.path.exists(dir):
            print(">>> Creating" + dir + "")
            os.mkdir(str(dir))
            print(">>> Created" + dir + "")
        else:
            print(">>> "+dir+" Already Exists")
        return True

    # Accepts File Array and Move files
    def move(self, src, dest_path):
        shutil.move(src, dest_path)

    # Accepts File Path and New name
    # Sample Input '/user/sagar/old_file.txt', 'new_file.txt'
    def rename(self, old_file_path, new_name):
        parent_dir = os.path.dirname(old_file_path)
        new_file_path = join(parent_dir, new_name)
        shutil.move(old_file_path, new_file_path)

    # Upload File
    def upload(self, file_dir, file):

        fs = FileSystemStorage(file_dir)
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url
