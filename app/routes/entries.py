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

entries_bp:Blueprint = Blueprint("entries", __name__, url_prefix="/api")

@entries_bp.route("/entries", methods=["POST"])
def add_entry() -> Response:
    return AddEntryService().add_entry()


@entries_bp.route("/entries", methods=["GET"])
def fetch_entries() -> Response:
    return GetEntryService().get_entries()


@entries_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
def delete_entry(entry_id: int) -> Response:
    return DeleteEntryService().delete_entry(entry_id)


@entries_bp.route("/entries/<int:entry_id>", methods=["PUT"])
def update_entry(entry_id: int) -> Response:
    return UpdateEntryService().update_entry(entry_id)