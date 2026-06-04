from flask import session, jsonify, Response
from app.models.entry import Entry
from typing import Tuple, Any

class GetEntryService:
    """Service to retrieve all tax deduction entries for the current user."""

    def __init__(self) -> None:
        """Initialize service with current user ID from session."""
        self.user_id: Any = session.get("user_id")

    def get_entries(self) -> Tuple[Response, int]:
        """Fetches all entries belonging to the user from the database."""
        if not self.user_id:
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        # Query database for all user-specific entries
        entries: Any = Entry.query.filter_by(user_id=self.user_id).all()

        return jsonify([
            {
                "id": e.id,
                "merchant": e.merchant,
                "amount": e.amount,
                "tax": e.tax,
                "category": e.category,
                "description": e.description,
                "date": e.date.isoformat(),
                "createdAt": e.created_at.isoformat() if e.created_at else None,
                "warrantyMonths": e.warranty_months,
                "warrantyExpiryDate": e.warranty_expiry_date.isoformat() if e.warranty_expiry_date else None
            }
            for e in entries # loop between each entry
        ]), 200