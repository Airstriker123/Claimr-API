from flask import Blueprint, jsonify ,Response
import time

home_bp = Blueprint('home', __name__)
START_TIME = time.time()


def get_uptime():
    total_seconds = int(time.time() - START_TIME)
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
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

