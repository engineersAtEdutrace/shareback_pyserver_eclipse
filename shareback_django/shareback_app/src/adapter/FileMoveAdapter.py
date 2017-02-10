from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileMoveResponseDTO import FileMoveResponseDTO
from shareback_app.src.service.FileMoveService import FileMoveService


class FileMoveAdapter(BaseAdapter):

    def execute(self):
        # Get Input Arguments
        src = str(self.request.GET.get(Constants.OLD_FILE_PATH, None))
        dest = str(self.request.GET.get(Constants.NEW_FILE_PATH, None))

        # Prepare Arguments
        src = self.path_converter.to_abs(src)
        dest = self.path_converter.to_abs(dest)

        # Call Service
        result = FileMoveService(self.user_id).move(src, dest)

        # Prepare Response
        response = FileMoveResponseDTO()
        response.result = result

        return response
