# this file automates the process of project setup
# Not related to program functionality.

import os
import random
import string

def banner() -> str:
    """banner printing function"""
    banner_text: str = \
r"""
__________                __                      .___    _____ __________.___ 
\______   \_____    ____ |  | __ ____   ____    __| _/   /  _  \\______   \   |
 |    |  _/\__  \ _/ ___\|  |/ // __ \ /    \  / __ |   /  /_\  \|     ___/   |
 |    |   \ / __ \\  \___|    <\  ___/|   |  \/ /_/ |  /    |    \    |   |   |
 |______  /(____  /\___  >__|_ \\___  >___|  /\____ |  \____|__  /____|   |___|
        \/      \/     \/     \/    \/     \/      \/          \/              
"""
    faded_banner: str = ""
    red: int = 40
    for line in banner_text.splitlines(): #format banner in a faded purple gradient
        faded_banner += f"\033[38;2;{red};0;220m{line}\033[0m\n"
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded_banner


def create_env() -> bool:
    """create an environment secret for application"""
    if not os.path.exists("app/.env"):
        random_string = ''.join(
            random.choices(
            string.ascii_letters + string.digits, k=67)
        )

        with open("app/.env", "w") as secret:
            # create a random secret key and write to file
            secret.write(f"SECRET_KEY={random_string}")
        return True
    return False

def clear() -> None:
    """clear the console"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# run the application
try:
    from app import main as application
except Exception as e:
    print(f"py packages not found...installing: \n errors: {e}")
    os.system("pip install -r requirements.txt")
    from app import main as application
app: app = application()

if __name__ == "__main__":
    # dev configs
    create_env()
    clear()
    print(banner())  # print banner
    app.run(
        # application configuration args
        debug=False,
        host="0.0.0.0",
        port=9988,
        threaded=True,
        use_reloader=True,
        use_debugger=False,
        use_evalex=True,
    )
