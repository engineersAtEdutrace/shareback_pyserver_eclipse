import json

from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileMkdirResponseDTO import FileMkdirResponseDTO
from shareback_app.src.service.FileMkdirService import FileMkdirService


class FileMkdirAdapter(BaseAdapter):

    def execute(self):

        # Get Input Arguments
        file_arr = str(self.request.GET.get(Constants.DIRECTORY_PATH, None))
        file_arr = json.loads(file_arr)

        # Prepare Arguments
        file_arr = self.path_converter.to_abs_arr(file_arr)

        # Call Service
        result = FileMkdirService(self.user_id).mkdir(file_arr)

        # Prepare Response
        response = FileMkdirResponseDTO()
        response.result = result

        return response
