from flask import Blueprint, jsonify

entries_bp = Blueprint("entries", __name__)

@entries_bp.route("/api/entries", methods=["POST"])
def add_entry():
    return jsonify({"message": "Add entry placeholder"})

@entries_bp.route("/api/entries", methods=["GET"])
def fetch_entries():
    return jsonify([])
