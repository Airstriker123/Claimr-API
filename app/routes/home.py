from flask import (
    Blueprint,
    jsonify ,
    Response
)
from app.extensions import limiter
from ..utils import get_uptime, success, warn

home_bp:Blueprint = Blueprint('home', __name__) # join file to blueprint project alias

@home_bp.route("/")
@limiter.limit("1/second;")
def home() -> Response:
    """home route for debug"""
    success(f"called message from BACKEND")
    return jsonify(
    {
            "message": "Awaiting requests!",
            "Status": "Online",
            "StatusCode": 200,
            "server-up-time": get_uptime(),
    }
)

@home_bp.route("/api/status")
@limiter.limit("1/second;")
def status() -> Response:
    """Get current status of API (for client checking)"""
    warn(f"client requested status")
    #Check if server responds to client
    return jsonify(
    {
            "Status": "Online",
    }
)
