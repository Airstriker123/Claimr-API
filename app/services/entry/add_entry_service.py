from app.models.entry import Entry
from datetime import datetime
from flask import (
    session,
    jsonify,
    request
)
from app.extensions import db
from typing import Tuple, Any, Dict


class AddEntryService:
    """Service to handle the creation of a single tax deduction entry."""

    def __init__(self) -> None:
        """Initialize service with user session and request data."""
        self.__user_id: Any = session.get("user_id")
        self.__data: Dict[Any, Any] | Any = request.get_json() or {}

    def __convert_date(self, key: str = "date") -> datetime:
        """Helper to convert ISO date strings to datetime objects, defaulting to current time."""
        date_str = self.__data.get(key)
        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            return datetime.utcnow()

    def add_entry(self) -> Tuple[Any, int]:
        """Validates request data and creates a new entry in the database."""
        if not self.__user_id: # check if client user is authenticated
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        data: Dict[Any, Any] | Any = self.__data

        # Basic validation for required fields
        if not data.get("merchant") or not data.get("amount"):
            return jsonify(
                {
                    "error": "Missing required fields"
                }
            ), 400

        try:
            amount: float  = float(data.get("amount"))
            tax: float = float(data.get("tax") or 0)
            
            warranty_months = None
            if data.get("warrantyMonths"):
                warranty_months = int(data.get("warrantyMonths"))
        except ValueError:
            return jsonify(
                {
                    "error": "Invalid number format"
                }
            ), 400

        expiry_date = None
        if data.get("warrantyExpiryDate"):
            try:
                # format the warranty expiry date received from frontend into datetime
                expiry_date = datetime.fromisoformat(data.get("warrantyExpiryDate"))
            except (TypeError, ValueError):
                pass

        # Construct and save entry
        entry: Entry = (Entry
        (
            merchant=data.get("merchant"),
            amount=amount,
            tax=tax,
            category=data.get("category"),
            description=data.get("description"),
            warranty_months=warranty_months,
            warranty_expiry_date=expiry_date,
            date=self.__convert_date("date"),
            created_at=self.__convert_date("createdAt"),
            user_id=self.__user_id
        ))

        db.session.add(entry)
        db.session.commit()

        return jsonify({
            "id": entry.id,
            "merchant": entry.merchant,
            "amount": entry.amount,
            "tax": entry.tax,
            "category": entry.category,
            "description": entry.description,
            "date": entry.date.isoformat(),
            "createdAt": entry.created_at.isoformat(),
            "warrantyMonths": entry.warranty_months,
            "warrantyExpiryDate": entry.warranty_expiry_date.isoformat() if entry.warranty_expiry_date else None
        }), 201
