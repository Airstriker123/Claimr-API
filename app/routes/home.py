from flask import Blueprint, jsonify ,Response, request, g
import time

home_bp = Blueprint('home', __name__)
START_TIME = time.time()

def get_client_ip():
    """
    Safely extract the client's IP address from the request.
    Handles cases where the app is behind a proxy/load balancer.
    """
    # Check for X-Forwarded-For header (may contain multiple IPs)
    if request.headers.getlist("X-Forwarded-For"):
        # Take the first IP in the list (original client)
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0].strip()
    else:
        # Fallback to direct remote address
        ip = request.remote_addr
    return ip

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
            "client_ip": get_client_ip(),
            "server-up-time": get_uptime(),
            "online": True,
    }
)

