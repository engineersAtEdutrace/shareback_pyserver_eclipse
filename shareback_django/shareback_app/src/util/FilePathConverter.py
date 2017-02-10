import os
import re
from os.path import expanduser, join
import os.path as path

from shareback_app.src.EnvConstants import EnvConstants
from shareback_app.src.exception.InputFormatException import InputFormatException
from shareback_app.src.util.FileOperations import FileOperations


class FilePathConverter:

    def __init__(self, user_id):
        self.user_id = user_id

        self.base_dir = expanduser(EnvConstants.BASE_DIR)

        # *** Compute user_id ***
        user_dir = ""+user_id
        self.home_dir = join(self.base_dir, user_dir)

        self.check_env()

    def check_env(self):
        # Check if BASE directory exists
        if not path.exists(self.base_dir):
            FileOperations(self.user_id).mkdir(self.base_dir)
        # Check if USER directory exists
        if not path.exists(self.home_dir):
            FileOperations(self.user_id).mkdir(self.home_dir)
            print(self.home_dir+" Created...")
        else:
            print(self.home_dir+" Exists...")

    def to_abs_arr(self, rel_path_arr):
        abs_path_arr = list()
        for rel_path in rel_path_arr:
            abs_path = self.to_abs(rel_path)
            abs_path_arr.append(abs_path)
        return abs_path_arr

    def to_abs(self, rel_path):
        # input checking
        if not str(rel_path).startswith("/"):
            raise InputFormatException("Expected format: /hello/something, Current format: "+rel_path)
        abs_path = self.home_dir+rel_path
        return abs_path

    def to_rel_arr(self, abs_path_arr):
        rel_path_arr = list()
        for abs_path in abs_path_arr:
            rel_path = self.to_rel(abs_path)
            rel_path_arr.append(rel_path)
        return rel_path_arr

    def to_rel(self, abs_path):
        rel_path = str(abs_path).replace(self.home_dir, "", count=1)
        return rel_path
