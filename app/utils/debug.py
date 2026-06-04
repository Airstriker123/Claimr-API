# utils/debug.py — debugging useful log messages
import traceback
from datetime import datetime
from colorama import Fore, init


init(autoreset=True) # terminal colour reset config set to true


# Colors formats for printing to console
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
    """Core Utility function to log a message to the console."""
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
    """Utility function to catch exceptions and log them to the console."""
    log(f"{context} -> {str(e)}", "ERROR")
    print(GREY + traceback.format_exc())


# ===== Success / Info helpers =====
def success(msg: str):
    """utility function to log a message to the console. If request is successful, log the success message."""
    log(msg, "SUCCESS")


def client_error(msg: str):
    """Utility function to log a error message to the console. If request from client IO is invalid"""
    log(msg, "Client I/O Error")


def warn(msg: str):
    """Utility function to log a warning message to the console.
    If an alert was triggered from client request"""
    log(msg, "WARN")


def info(msg: str):
    """Utility function to log an info message to the console. """
    log(msg, "INFO")