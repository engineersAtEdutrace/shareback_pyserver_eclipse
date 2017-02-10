from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FeedbackInsertResponseDTO import FeedbackInsertResponseDTO
from shareback_app.src.service.FeedbackInsertService import FeedbackInsertService


class FeedbackInsertAdapter(BaseAdapter):

    def execute(self):

        # Prepare Service Input Arguments
        session_id = str(self.request.GET.get(Constants.SESSION_ID, None))
        rating = int(self.request.GET.get(Constants.RATING, None))
        comment = str(self.request.GET.get(Constants.COMMENT, None))

        # Call Service
        response = FeedbackInsertService(self.user_id).insert(session_id, comment, rating)

        # Prepare Response
        response_dto = FeedbackInsertResponseDTO()
        response_dto.result = response

        return response_dto
