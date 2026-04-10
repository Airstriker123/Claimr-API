from flask import Blueprint, jsonify, Response

entries_bp:Blueprint = Blueprint("entries", __name__)

@entries_bp.route("/entries", methods=["POST"])
def add_entry() -> Response:
    return jsonify(
        {
            "message": "Add entry placeholder"
        }
    )


@entries_bp.route("/entries", methods=["GET"])
def fetch_entries() -> Response:
    return jsonify([])
