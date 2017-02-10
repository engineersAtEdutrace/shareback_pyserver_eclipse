import sys

from shareback_app.models import Feedbacks, Sessions
from shareback_app.src.service.base.BaseService import BaseService


class FeedbackInsertService(BaseService):

    def insert(self, session_id, comment, rating):

        # ***Possible Consistency Problem***
        # Transaction Start
        session_entity = Sessions.objects.get(pk=session_id)
        feedback = Feedbacks()
        feedback.session_id = session_entity
        feedback.comment = comment
        feedback.save()

        switcher = {
            1: session_entity.rating_1,
            2: session_entity.rating_2,
            3: session_entity.rating_3,
            4: session_entity.rating_4,
            5: session_entity.rating_5,
        }
        if rating == 1:
            session_entity.rating_1 = switcher[rating] + 1
        if rating == 2:
            session_entity.rating_2 = switcher[rating] + 1
        if rating == 3:
            session_entity.rating_3 = switcher[rating] + 1
        if rating == 4:
            session_entity.rating_4 = switcher[rating] + 1
        if rating == 5:
            session_entity.rating_5 = switcher[rating] + 1

        # switcher[rating] += 1
#        print("Rating ", switcher[rating])
        session_entity.save()
        # --Transaction End

        response = True
        return response


