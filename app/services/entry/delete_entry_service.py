from typing import Tuple , Any

from flask import session, jsonify, Response
from app.models.entry import Entry
from app.extensions import db

class DeleteEntryService:
    """Service to handle the deletion of a tax deduction entry."""

    def __init__(self) -> None:
        """Initialize service with current user ID from session."""
        self.user_id: Any = session.get("user_id")

    def delete_entry(self, entry_id: int) -> Tuple[Response, int]:
        """Removes an entry from the database after verifying ownership."""
        if not self.user_id:
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        entry: Any = Entry.query.get(entry_id)

        # Security check: ensure entry exists and belongs to the current user
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