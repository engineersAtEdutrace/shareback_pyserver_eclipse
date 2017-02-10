from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse
from shareback_app.src.util.MyEncoder import MyEncoder


class FeedbackGetResponseDTO(BaseResponse):

    def __init__(self):
        self.comments = None
        self.session_id = None

    def __str__(self):
        return MyEncoder().encode(self)
