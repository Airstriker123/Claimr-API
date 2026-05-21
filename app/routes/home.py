from flask import (
    Blueprint,
    jsonify ,
    Response
)
from app.extensions import limiter
from ..utils import get_uptime, success, warn

home_bp:Blueprint = Blueprint('home', __name__)

@home_bp.route("/")
@limiter.limit("50/hour;20/minute;1/second")
def home() -> Response:
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
@limiter.limit("50/hour;1/second;5/minute")
def status() -> Response:
    warn(f"client requested status")
    return jsonify(
    {
            "Status": "Online",
    }
)
