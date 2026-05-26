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
    """Service to handle updating an existing tax deduction entry."""

    def __init__(self) -> None:
        """Initialize service with user session and update data from request."""
        self.user_id: Any = session.get("user_id")
        self.data: Dict[Any, Any] | Any  = request.get_json() or {}

    def __convert_date(self) -> datetime | None:
        """Convert ISO date string from update payload to datetime."""
        try:
            return datetime.fromisoformat(self.data.get("date"))
        except Exception as e:
            print(e)
            return None

    def update_entry(self, entry_id: int) -> Tuple[Any, int]:
        """Validates and updates specific fields of an entry in the database."""
        if not self.user_id:
            return jsonify({"error": "Unauthorized"}), 401

        entry: Any = Entry.query.get(entry_id)

        # Security check: ensure entry exists and belongs to the current user
        if not entry or entry.user_id != self.user_id:
            return jsonify(
                {
                    "error": "Not found"
                }
            ), 404

        # Update fields safely based on presence in request data
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

        if "warrantyMonths" in self.data:
            try:
                entry.warranty_months = int(self.data["warrantyMonths"]) if self.data["warrantyMonths"] else None
            except ValueError:
                pass

        if "warrantyExpiryDate" in self.data:
            try:
                entry.warranty_expiry_date = datetime.fromisoformat(self.data["warrantyExpiryDate"]) if self.data["warrantyExpiryDate"] else None
            except (TypeError, ValueError):
                pass

        db.session.commit()

        return jsonify(
            {
                "message": "Entry updated"
            }
        ), 200