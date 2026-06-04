from flask import session , jsonify
from typing import Tuple, Dict


class WipeSessionService:
    """Backend logic of Logging user of
    client and removing current session
    """

    @staticmethod
    def wipe_session() -> Tuple[Dict[str, str], int]:
        """Method for wiping session (triggers if client logs out of device)"""
        session.clear() # clear session (makes current session invalid to client) -- auto logs out
        return jsonify(
            {
                "message": "Session cleared!"
            }
        ), 200



