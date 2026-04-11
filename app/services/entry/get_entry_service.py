from flask import session, jsonify, Response
from app.models.entry import Entry
from typing import Tuple, Any

class GetEntryService:

    def __init__(self) -> None:
        self.user_id: Any = session.get("user_id")

    def get_entries(self) -> Tuple[Response, int]:
        if not self.user_id:
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        entries: Any = Entry.query.filter_by(user_id=self.user_id).all()

        return jsonify([
            {
                "id": e.id,
                "merchant": e.merchant,
                "amount": e.amount,
                "tax": e.tax,
                "category": e.category,
                "description": e.description,
                "date": e.date.isoformat()
            }
            for e in entries
        ]), 200