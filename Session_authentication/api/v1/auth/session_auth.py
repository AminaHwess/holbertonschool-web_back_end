#!/usr/bin/env python3
"""Session authentication"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session method that creates a Session ID for a user_id"""

        if user_id is None or type(user_id) != str:
            return None
        sessionId = str(uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId
