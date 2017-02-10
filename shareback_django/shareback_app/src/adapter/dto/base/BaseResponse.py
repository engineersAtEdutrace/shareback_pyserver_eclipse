from shareback_app.src.util.MyEncoder import MyEncoder


class BaseResponse:

    def __str__(self):
        return MyEncoder().encode(self)
