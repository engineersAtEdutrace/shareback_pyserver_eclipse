from datetime import datetime as timestamp

import hashlib

from shareback_app.models import Sessions
from shareback_app.src.service.base.BaseService import BaseService
from shareback_app.src.util.DateFormatter import DateFormatter


class StartSessionService(BaseService):

    def start(self, session_name):
        sessions = Sessions()
        cur_timestamp = DateFormatter.format(timestamp.now())
        en_name = session_name+cur_timestamp
        m = hashlib.md5()
        m.update(en_name)
        session_id = m.hexdigest()

        sessions.session_id = session_id
        sessions.session_name = session_name
        sessions.save()

        return session_id


