from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.FeedbackGetResponseDTO import FeedbackGetResponseDTO
from shareback_app.src.service.FeedbackGetService import FeedbackGetService


class FeedbackGetAdapter(BaseAdapter):

    def execute(self):
        # Prepare Input Arguments
        session_id = self.request.GET.get(Constants.SESSION_ID, None)

        # Call service
        comments = FeedbackGetService(self.user_id).get_comments(session_id)

        # Prepare Response
        response_dto = FeedbackGetResponseDTO()
        response_dto.session_id = session_id
        response_dto.comments = comments

        return response_dto
