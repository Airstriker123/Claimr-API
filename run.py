class Banner(object):
    """
    class stores look of banner
    - cosmetic for terminal does nothing but display server text development
    """

    def __init__(self) -> None:
        self.banner = \
r"""
__________                __                      .___    _____ __________.___ 
\______   \_____    ____ |  | __ ____   ____    __| _/   /  _  \\______   \   |
 |    |  _/\__  \ _/ ___\|  |/ // __ \ /    \  / __ |   /  /_\  \|     ___/   |
 |    |   \ / __ \\  \___|    <\  ___/|   |  \/ /_/ |  /    |    \    |   |   |
 |______  /(____  /\___  >__|_ \\___  >___|  /\____ |  \____|__  /____|   |___|
        \/      \/     \/     \/    \/     \/      \/          \/              
"""

        self.faded_banner = Banner.purplepink(self.banner)

    @staticmethod
    def purplepink(text) -> str:
        """
        method to print a banner gradient purple gradient in this case
        """
        faded = ""
        red = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded


def main() -> bool:
    from app import create_app
    app = create_app()
    if __name__ == "__main__":
        print(Banner().faded_banner)  # print banner
        app.run(debug=True, host="0.0.0.0", port=9988)
        return True
    return False
main()