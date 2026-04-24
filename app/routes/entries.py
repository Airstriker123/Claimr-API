from flask import (
    Blueprint,
    jsonify,
    Response,
    request
)
from ..services.entry.get_entry_service import GetEntryService
from ..services.entry.update_entry_service import UpdateEntryService
from ..services.entry.add_entry_service import AddEntryService
from ..services.entry.delete_entry_service import DeleteEntryService

from typing import Tuple

entries_bp:Blueprint = Blueprint("entries", __name__, url_prefix="/api")

@entries_bp.route("/entries", methods=["POST"])
def add_entry() -> Tuple[Response, int] | int:
    try:
        return (
            AddEntryService().add_entry(),
            200
        )
    except Exception as e:
        print(f"[ERROR] failed to add entry\n{e}")
        return 500


@entries_bp.route("/entries", methods=["GET"])
def fetch_entries() -> Tuple[Response, int] | int:
    try:
        return (
            GetEntryService().get_entries(),
            200
        )
    except Exception as e:
        print(f"[ERROR] failed to fetch entries\n{e}")
        return 500



@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
def delete_entry(entry_id: int) -> Tuple[Response, int] | int:
    try:
        return (
            DeleteEntryService().delete_entry(entry_id),
            200
        )
    except Exception as e:
        print(f"[ERROR] failed to delete entry\n{e}")
        return 500


@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
def update_entry(entry_id: int) -> Tuple[Response, int] | int:
    try:
        return (
            UpdateEntryService().update_entry(entry_id),
            200
        )
    except Exception as e:
        print(f"[ERROR] failed to update entry\n{e}")
        return 500