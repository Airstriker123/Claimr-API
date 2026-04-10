from flask import Blueprint, jsonify ,Response
import time

home_bp:Blueprint = Blueprint('home', __name__)
START_TIME:float = time.time()


def get_uptime() -> str:
    total_seconds:float = int(time.time() - START_TIME)
    days:float = total_seconds // 86400
    hours:float = (total_seconds % 86400) // 3600
    minutes:float = (total_seconds % 3600) // 60
    seconds:float = total_seconds % 60
    return (f"{days} days, "
            f"{hours} hours, "
            f"{minutes} minutes,"
            f" {seconds}seconds")

@home_bp.route("/")
def home() -> Response:
    print(f"SUCCESS -- called message from BACKEND")
    return jsonify(
    {
            "message": "Awaiting requests!",
            "Status": "Online",
            "StatusCode": 200,
            "server-up-time": get_uptime(),
    }
)

@home_bp.route("/api/status")
def status() -> Response:
    print(f"SUCCESS -- called message from BACKEND")
    return jsonify(
    {
            "Status": "Online",
    }
)
