import json

from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileCopyResponseDTO import FileCopyResponseDTO
from shareback_app.src.service.FileCopyService import FileCopyService


class FileCopyAdapter(BaseAdapter):

    def execute(self):

        # Get Input Arguments
        src_file_arr = json.loads(
            self.request.GET.get(Constants.FILE_PATH_ARRAY, None)
        )
        dest_path = self.request.GET.get(Constants.DESTINATION_PATH, None)

        # Prepare Arguments
        src_file_arr = self.path_converter.to_abs_arr(src_file_arr)
        dest_path = self.path_converter.to_abs(dest_path)

        # Call Service
        result = FileCopyService(self.user_id).copy(src_file_arr, dest_path)

        # Prepare Response
        response = FileCopyResponseDTO()
        response.result = result

        return response