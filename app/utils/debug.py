# utils/debug.py
import traceback
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# Colors
RED = Fore.RED
ORANGE = '\033[38;5;208m'
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
GREY = Fore.LIGHTBLACK_EX
PURPLE = Fore.MAGENTA
RESET = Fore.RESET

# ===== Core Logger =====
def log(message: str, level: str = "INFO"):
    time = datetime.now().strftime("%H:%M:%S")

    color = {
        "INFO": CYAN,
        "SUCCESS": GREEN,
        "WARN": YELLOW,
        "ERROR": RED,
        "Client I/O Error": ORANGE,
    }.get(level, CYAN)

    print(f"{PURPLE}[{RESET}{time}{PURPLE}]{RESET} {color}[{level}] {RESET}{message}")


# ===== Error Handler =====
def error_crash(e: Exception, context: str = ""):
    print(GREY + traceback.format_exc())
    log(f"{context} -> {str(e)}", "ERROR")

# ===== Success / Info helpers =====
def success(msg: str):
    log(msg, "SUCCESS")

def client_error(msg: str):
    log(msg, "Client I/O Error")

def warn(msg: str):
    log(msg, "WARN")

def info(msg: str):
    log(msg, "INFO")