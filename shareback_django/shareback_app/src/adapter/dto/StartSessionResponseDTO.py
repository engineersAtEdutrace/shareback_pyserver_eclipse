from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse
from shareback_app.src.util.MyEncoder import MyEncoder


class StartSessionResponseDTO(BaseResponse):
    def __init__(self):
        self.session_id = None
        self.session_name = None
