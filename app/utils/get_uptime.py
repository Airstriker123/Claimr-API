import time


START_TIME: float = time.time()


def get_uptime() -> str:
    total_seconds: float = int(time.time() - START_TIME)
    days: float = total_seconds // 86400
    hours: float = (total_seconds % 86400) // 3600
    minutes: float = (total_seconds % 3600) // 60
    seconds: float = total_seconds % 60
    return (
        f"{days} days, "
        f"{hours} hours, "
        f"{minutes} minutes,"
        f" {seconds}seconds"
    )
