from flask import (
    Blueprint,
    Response,
    jsonify
)
from ..services.entry.get_entry_service import GetEntryService
from ..services.entry.update_entry_service import UpdateEntryService
from ..services.entry.add_entry_service import AddEntryService
from ..services.entry.add_batch_entries_service import AddBatchEntriesService
from ..services.entry.delete_entry_service import DeleteEntryService
from app.extensions import limiter
from typing import Tuple


# path config — joins route to blueprint project
entries_bp: Blueprint = Blueprint("entries", __name__, url_prefix="/api")

@entries_bp.route("/entries", methods=["POST"])
@limiter.limit("100/minute;2/second")
def add_entry() -> Tuple[Response, int]:
    """Route to add a new entry to the database"""
    try:
        return AddEntryService().add_entry() #get response
    except Exception as e:
        print(f"[ERROR] failed to add entry\n{e}")
        return jsonify({"error": "Internal Server Error"}), 500


@entries_bp.route("/entries/batch", methods=["POST"])
@limiter.limit("50/minute;5/second")
def add_entries_batch() -> Tuple[Response, int]:
    """Route to add multiple entries to the database"""
    try:
        return AddBatchEntriesService().add_entries() #get response
    except Exception as e:
        print(f"[ERROR] failed to add batch entries\n{e}")
        return jsonify({"error": "Internal Server Error"}), 500


@entries_bp.route("entries", methods=["GET"])
@limiter.limit("200/minute;50/second") # prevents malicious tools from mass spamming entry requests
def fetch_entries() -> Tuple[Response, int]:

    """Route to fetch all entries from the database"""
    try:
        return GetEntryService().get_entries() #get response

    except Exception as e:
        print(f"[ERROR] failed to fetch entries\n{e}")
        return jsonify({"error": "Internal Server Error"}), 500

@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
@limiter.limit("80/minute;")
def delete_entry(entry_id: int) -> Tuple[Response, int]:
    """Route to delete an entry from the database"""
    try:
        return DeleteEntryService().delete_entry(entry_id) #get response

    except Exception as e:
        print(f"[ERROR] failed to delete entry\n{e}")
        return jsonify({"error": "Internal Server Error"}), 500


@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
@limiter.limit("80/minute;")
def update_entry(entry_id: int) -> Tuple[Response, int]:
    """Route to update an entry from the database"""
    try:
        return UpdateEntryService().update_entry(entry_id) #get response
    except Exception as e:
        print(f"[ERROR] failed to update entry\n{e}")
        return jsonify({"error": "Internal Server Error"}), 500