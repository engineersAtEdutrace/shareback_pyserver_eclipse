from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse


class FileLsResponseDTO(BaseResponse):

    def __init__(self):
        self.result = None

    # def set_result(self, result):
    #     self.result = result
    #
    # def get_dir(self):
    #     return self.dir
