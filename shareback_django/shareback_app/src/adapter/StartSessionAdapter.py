from shareback_app.src.Constants import Constants
from shareback_app.src.adapter.base.BaseAdapter import BaseAdapter
from shareback_app.src.adapter.dto.StartSessionResponseDTO import StartSessionResponseDTO
from shareback_app.src.service.StartSessionService import StartSessionService


class StartSessionAdapter(BaseAdapter):
    def execute(self):
        # Prepare Input Arguments
        session_name = self.request.GET.get(Constants.SESSION_NAME, None)

        # Call Service
        session_id = StartSessionService(self.user_id).start(session_name)

        # Prepare Response
        response = StartSessionResponseDTO()
        response.session_id = session_id
        response.session_name = session_name

        return response