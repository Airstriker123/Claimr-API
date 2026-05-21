from flask import session , jsonify
from typing import Tuple, Dict


class WipeSessionService:
    """Backend logic of Logging user of
    client and removing current session
    """

    @staticmethod
    def wipe_session() -> Tuple[Dict[str, str], int]:
        """Method for wiping session"""
        session.clear() # clear session (makes current session invalid to client) -- auto logs out
        return \
        {
                "message": "Session cleared!"
        }, 200



