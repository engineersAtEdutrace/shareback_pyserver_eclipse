from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse


class RegisterRequestDTO(BaseResponse):

    def __init__(self):
        self.result = None
