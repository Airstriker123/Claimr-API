from typing import Any, Dict, Tuple
from flask import (
    session,
    jsonify,
    request
)
from app.models.entry import Entry
from app.extensions import db
from datetime import datetime


class UpdateEntryService:


    def __init__(self) -> None:

        self.user_id: Any = session.get("user_id")
        self.data: Dict[Any, Any] | Any  = request.get_json() or {}


    def __convert_date(self) -> datetime | None:
        try:
            return datetime.fromisoformat(self.data.get("date"))
        except Exception as e:
            print(e)
            return None


    def update_entry(self, entry_id: int) -> Tuple[Any, int]:
        if not self.user_id:
            return jsonify({"error": "Unauthorized"}), 401

        entry: Any = Entry.query.get(entry_id)

        # security check
        if not entry or entry.user_id != self.user_id:
            return jsonify(
                {
                    "error": "Not found"
                }
            ), 404

        # update fields safely
        if "merchant" in self.data:
            entry.merchant = self.data["merchant"]

        if "amount" in self.data:
            try:
                entry.amount = float(self.data["amount"])
            except ValueError:
                return jsonify(
                    {
                        "error": "Invalid amount"
                    }
                ), 400

        if "tax" in self.data:
            try:
                entry.tax = float(self.data["tax"])
            except ValueError:
                return jsonify(
                    {
                        "error": "Invalid tax"
                    }
                ), 400

        if "category" in self.data:
            entry.category = self.data["category"]

        if "description" in self.data:
            entry.description = self.data["description"]

        if "date" in self.data:
            new_date: datetime = self.__convert_date()
            if new_date:
                entry.date = new_date

        db.session.commit()

        return jsonify(
            {
                "message": "Entry updated"
            }
        ), 200