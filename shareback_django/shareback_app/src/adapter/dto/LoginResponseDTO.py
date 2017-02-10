from shareback_app.src.adapter.dto.base.BaseResponse import BaseResponse


class LoginResponseDTO(BaseResponse):
    # def set_login_token(self, session_token):
    #     self.session_token = session_token

    def __init__(self):
        self.session_token = None
