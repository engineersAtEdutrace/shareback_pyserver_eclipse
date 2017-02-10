import json

from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileDeleteResponseDTO import FileDeleteResponseDTO
from shareback_app.src.service.FileDeleteService import FileDeleteService


class FileDeleteAdapter(BaseAdapter):

    def execute(self):

        # Get Input Arguments
        file_arr = json.loads(
            str(self.request.GET.get(Constants.FILE_PATH_ARRAY, None))
        )

        # Prepare Input Arguments
        file_arr = self.path_converter.to_abs_arr(file_arr)

        # Call Service
        result = FileDeleteService(self.user_id).delete(file_arr)

        # Prepare Response
        response = FileDeleteResponseDTO()
        response.result = result

        return response
