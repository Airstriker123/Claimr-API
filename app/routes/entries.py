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


# path config — joins route to blueprint project
entries_bp: Blueprint = Blueprint("entries", __name__, url_prefix="/api")

@entries_bp.route("/entries", methods=["POST"])
@limiter.limit("150/day;20/minute;1/second")
def add_entry() -> Tuple[Response, int] | int:
    """Route to add a new entry to the database"""
    try:
        return AddEntryService().add_entry() #get response
    except Exception as e:
        print(f"[ERROR] failed to add entry\n{e}")
        return 500


@entries_bp.route("/entries", methods=["GET"])
@limiter.limit("3/second")
def fetch_entries() -> Tuple[Response, int] | int:
    """Route to fetch all entries from the database"""
    try:
        return GetEntryService().get_entries() #get response

    except Exception as e:
        print(f"[ERROR] failed to fetch entries\n{e}")
        return 500



@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
@limiter.limit("2/second")
def delete_entry(entry_id: int) -> Tuple[Response, int] | int:
    """Route to delete an entry from the database"""
    try:
        return DeleteEntryService().delete_entry(entry_id) #get response

    except Exception as e:
        print(f"[ERROR] failed to delete entry\n{e}")
        return 500


@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
@limiter.limit("200/day;25/minute;1/second")
def update_entry(entry_id: int) -> Tuple[Response, int] | int:
    """Route to update an entry from the database"""
    try:
        return UpdateEntryService().update_entry(entry_id) #get response
    except Exception as e:
        print(f"[ERROR] failed to update entry\n{e}")
        return 500