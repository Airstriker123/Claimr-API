import os
import random
import string

def banner() -> str:
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
    for line in banner_text.splitlines():
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

def start() -> bool:
    """run application"""
    try:
        from app import main as application
    except Exception as e:
        print(f"py packages not found...installing: \n errors: {e}")
        os.system("pip install -r requirements.txt")
        from app import main as application
    app: app = application()
    if __name__ == "__main__":
        #dev configs
        create_env()
        print(banner())  # print banner
        app.run(
            debug=True,
            host="0.0.0.0",
            port=9988,
            threaded=True,
            use_reloader=True,
            use_debugger=True,
            use_evalex=True,
        )
        return True
    #production configs
    return False
start()