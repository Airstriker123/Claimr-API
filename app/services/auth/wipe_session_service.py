from flask import session , jsonify
from typing import Tuple, Dict


class WipeSessionService:

    @staticmethod
    def wipe_session() -> Tuple[Dict[str, str], int]:
        session.clear()
        return \
        {
                "message": "Session cleared!"
        }, 200



