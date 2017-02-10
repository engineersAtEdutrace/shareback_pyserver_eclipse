import json

from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileLsResponseDTO import FileLsResponseDTO
from shareback_app.src.service.FileLsService import FileLsService


class FileLsAdapter (BaseAdapter):

    def execute(self):
        # Get Input Arguments
        dir = str(self.request.GET.get(Constants.FILE_PATH, None))
        print("FileLsAdapter upper: "+dir)

        # Prepare Arguments
        print("FileLsAdapter upper: "+dir)
        dir = self.path_converter.to_abs(dir)

        # Call Service
        print("FileLsAdapter: "+dir)
        result = FileLsService(self.user_id).ls(dir)

        # Prepare Response
        response = FileLsResponseDTO()
        response.result = result

        return response
