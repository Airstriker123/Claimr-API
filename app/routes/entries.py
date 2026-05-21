from flask import (
    Blueprint,
    Response,
)
from ..services.entry.get_entry_service import GetEntryService
from ..services.entry.update_entry_service import UpdateEntryService
from ..services.entry.add_entry_service import AddEntryService
from ..services.entry.delete_entry_service import DeleteEntryService
from app.extensions import limiter
from typing import Tuple

entries_bp:Blueprint = Blueprint("entries", __name__, url_prefix="/api")

@entries_bp.route("/entries", methods=["POST"])
@limiter.limit("150/day;20/minute;1/second")
def add_entry() -> Tuple[Response, int] | int:
    try:
        return AddEntryService().add_entry()
    except Exception as e:
        print(f"[ERROR] failed to add entry\n{e}")
        return 500


@entries_bp.route("/entries", methods=["GET"])
@limiter.limit("3/second")
def fetch_entries() -> Tuple[Response, int] | int:
    try:
        return GetEntryService().get_entries()

    except Exception as e:
        print(f"[ERROR] failed to fetch entries\n{e}")
        return 500



@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
@limiter.limit("2/second")
def delete_entry(entry_id: int) -> Tuple[Response, int] | int:
    try:
        return DeleteEntryService().delete_entry(entry_id)

    except Exception as e:
        print(f"[ERROR] failed to delete entry\n{e}")
        return 500


@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
@limiter.limit("200/day;25/minute;1/second")
def update_entry(entry_id: int) -> Tuple[Response, int] | int:
    try:
        return UpdateEntryService().update_entry(entry_id)
    except Exception as e:
        print(f"[ERROR] failed to update entry\n{e}")
        return 500