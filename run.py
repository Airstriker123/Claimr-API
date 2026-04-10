import os

class Banner(object):
    """
    class stores look of banner
    - cosmetic for terminal does nothing but display server text development
    """

    def __init__(self) -> None:
        self.banner: str = \
r"""
__________                __                      .___    _____ __________.___ 
\______   \_____    ____ |  | __ ____   ____    __| _/   /  _  \\______   \   |
 |    |  _/\__  \ _/ ___\|  |/ // __ \ /    \  / __ |   /  /_\  \|     ___/   |
 |    |   \ / __ \\  \___|    <\  ___/|   |  \/ /_/ |  /    |    \    |   |   |
 |______  /(____  /\___  >__|_ \\___  >___|  /\____ |  \____|__  /____|   |___|
        \/      \/     \/     \/    \/     \/      \/          \/              
"""

        self.faded_banner:str = Banner.purplepink(self.banner)

    @staticmethod
    def purplepink(text) -> str:
        """
        method to print a banner gradient purple gradient in this case
        """
        faded: str = ""
        red: int = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded


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
        print(Banner().faded_banner)  # print banner
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