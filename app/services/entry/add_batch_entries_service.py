from app.models.entry import Entry
from datetime import datetime
from flask import (
    session,
    jsonify,
    request
)
from app.extensions import db
from typing import Tuple, Any, Dict, List


class AddBatchEntriesService:
    """Service to handle the creation of multiple tax deduction entries in a single request."""

    def __init__(self) -> None:
        """Initialize service with user session and list of entry data."""
        self.__user_id: Any = session.get("user_id")
        self.__data: List[Dict[Any, Any]] | Any = request.get_json() or []

    def __convert_date(self, data: Dict[Any, Any], key: str = "date") -> datetime:
        """Convert string date from payload to datetime object."""
        date_str = data.get(key)
        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            return datetime.utcnow()

    def add_entries(self) -> Tuple[Any, int]:
        """Processes a list of entries, saves valid ones to the database, and returns results."""
        if not self.__user_id:
            return jsonify({"error": "Unauthorized"}), 401

        if not isinstance(self.__data, list):
            return jsonify({"error": "Expected a list of entries"}), 400

        results = []
        try:
            for entry_data in self.__data:
                try:
                    # Validate required fields for each entry in batch
                    if not entry_data.get("merchant") or not entry_data.get("amount"):
                        results.append({"error": "Missing required fields", "synced": False})
                        continue

                    amount = float(entry_data.get("amount"))
                    tax = float(entry_data.get("tax") or 0)
                    warranty_months = int(entry_data.get("warrantyMonths")) if entry_data.get("warrantyMonths") else None
                    
                    expiry_date = None
                    if entry_data.get("warrantyExpiryDate"):
                        try:
                            expiry_date = datetime.fromisoformat(entry_data.get("warrantyExpiryDate"))
                        except (TypeError, ValueError):
                            pass

                    # Construct entry model
                    entry = Entry(
                        merchant=entry_data.get("merchant"),
                        amount=amount,
                        tax=tax,
                        category=entry_data.get("category"),
                        description=entry_data.get("description"),
                        warranty_months=warranty_months,
                        warranty_expiry_date=expiry_date,
                        date=self.__convert_date(entry_data, "date"),
                        created_at=self.__convert_date(entry_data, "createdAt"),
                        user_id=self.__user_id
                    )
                    db.session.add(entry)
                    db.session.flush() # Generate ID for the response object

                    results.append({
                        "id": entry.id,
                        "merchant": entry.merchant,
                        "amount": entry.amount,
                        "tax": entry.tax,
                        "category": entry.category,
                        "description": entry.description,
                        "date": entry.date.isoformat(),
                        "createdAt": entry.created_at.isoformat(),
                        "warrantyMonths": entry.warranty_months,
                        "warrantyExpiryDate": entry.warranty_expiry_date.isoformat() if entry.warranty_expiry_date else None,
                        "synced": True
                    })
                except Exception as e:
                    print(f"[ERROR] Entry processing failed: {e}")
                    results.append({"error": str(e), "synced": False})

            db.session.commit()
            return jsonify(results), 201

        except Exception as e:
            db.session.rollback()
            print(f"[ERROR] Batch commit failed: {e}")
            return jsonify({"error": "Failed to add entries"}), 500
