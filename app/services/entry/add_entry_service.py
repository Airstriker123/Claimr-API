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


    def __init__(self) -> None:
        self.__user_id: Any = session.get("user_id")
        self.__data: Dict[Any, Any] | Any = request.get_json() or {}


    def __convert_date(self) -> datetime:
        # convert string to datetime
        date_str = self.__data.get("date")
        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            return datetime.utcnow()


    def add_entry(self) -> Tuple[Any, int]:
        if not self.__user_id:
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        data: Dict[Any, Any] | Any = self.__data

        if not data.get("merchant") or not data.get("amount"):
            return jsonify(
                {
                    "error": "Missing required fields"
                }
            ), 400

        try:
            amount: float  = float(data.get("amount"))
            tax: float = float(data.get("tax") or 0)
        except ValueError:
            return jsonify(
                {
                    "error": "Invalid number format"
                }
            ), 400

        entry: Entry = (Entry
        (
            merchant=data.get("merchant"),
            amount=amount,
            tax=tax,
            category=data.get("category"),
            description=data.get("description"),
            date=self.__convert_date(),
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
            "date": entry.date.isoformat()
        }), 201
