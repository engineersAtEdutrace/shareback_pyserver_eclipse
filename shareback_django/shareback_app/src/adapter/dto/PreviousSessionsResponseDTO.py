from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse
from shareback_app.src.util.MyEncoder import MyEncoder


class PreviousSessionsResponseDTO(BaseResponse):

    # def set_session_list(self, session_list):
    #     self.session_list = session_list

    def __init__(self):
        self.session_list = None


class SessionMetadata:
    def set_session_id(self, session_id):
        self.session_id = session_id

    def set_session_name(self, session_name):
        self.session_name = session_name

    def set_date(self, date):
        self.date = date

    def get_session_id(self):
        return self.session_id

    def get_session_name(self):
        return self.session_name

    def get_date(self):
        return self.date

    def __init__(self):
        self.session_id = None
        self.session_name = None
        self.date = None
