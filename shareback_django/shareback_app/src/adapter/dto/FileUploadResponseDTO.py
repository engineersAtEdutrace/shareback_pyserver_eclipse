from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse


class FileUploadResponseDTO(BaseResponse):

    # def set_result(self, result):
    #     self.result = result

    def __init__(self):
        self.result = False
