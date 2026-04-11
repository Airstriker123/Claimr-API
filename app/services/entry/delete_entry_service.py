from typing import Tuple , Any

from flask import session, jsonify, Response
from app.models.entry import Entry
from app.extensions import db

class DeleteEntryService:

    def __init__(self) -> None:
        self.user_id: Any = session.get("user_id")

    def delete_entry(self, entry_id: int) -> Tuple[Response, int]:
        if not self.user_id:
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        entry: Any = Entry.query.get(entry_id)

        # security check
        if not entry or entry.user_id != self.user_id:
            return jsonify(
                {
                    "error": "Not found"
                }
            ), 404

        db.session.delete(entry)
        db.session.commit()

        return jsonify(
            {
                "message": "Entry deleted"
            }
        ), 200