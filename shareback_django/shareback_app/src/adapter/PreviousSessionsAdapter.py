from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.PreviousSessionsResponseDTO import PreviousSessionsResponseDTO
from shareback_app.src.service.PreviousSessionsSerivce import PreviousSessionsService


class PreviousSessionsAdapter(BaseAdapter):

    def execute(self):

        # Prepare Input Arguments
        request_no = int(
            self.request.GET.get(Constants.SESSION_ID, None)
        )

        # Call service
        sessions_list = PreviousSessionsService(self.user_id).get_list(request_no)

        # Prepare Response
        response_dto = PreviousSessionsResponseDTO()
        response_dto.session_list = sessions_list

        return response_dto
