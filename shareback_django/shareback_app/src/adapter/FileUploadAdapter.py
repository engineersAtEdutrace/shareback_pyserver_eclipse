from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FileUploadResponseDTO import FileUploadResponseDTO
from shareback_app.src.service.FileUploadService import FileUploadService


class FileUploadAdapter(BaseAdapter):
    def execute(self):

        # Get Input Arguments
        request = self.request
        if request.method == 'POST' and request.FILES[Constants.FILE_TO_UPLOAD]:
            file = request.FILES[Constants.FILE_TO_UPLOAD]
            file_dir = request.POST.get(Constants.DIRECTORY_PATH)
        else:
            return FileUploadResponseDTO()

        # Prepare Arguments
        file_dir = self.path_converter.to_abs(file_dir)

        # Call Service
        result = FileUploadService(self.user_id).upload(file_dir, file)

        # Prepare Response
        response = FileUploadResponseDTO()
        response.result = result

        return response
