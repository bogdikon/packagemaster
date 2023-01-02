# Simple py ColorLogger by Bogdikon with love <3
#
#   Purpose: Color logs
#
#
################################

__version__ = 1.0
__author__ = "Bogdikon"


class Color:
    DEFAULT = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    LBLUE = "\033[36m"
    LIGHT = "\033[1m"
    DIM = "\033[2m"
    ERR_BLINK = "\033[7m"
    CROSSED_OUT = "\033[9m"
    DOUBLE_UNDERLINE = "\033[21m"
    BLINK_END = "\033[25m"
    DIMGREEN = "\033[38;5;107m"


def log(status: str, msg: str):
    """

    :param status: Error Status, Can be ok, err, warn, info
    :param msg: Message
    :return: Formatted string
    """
    if status == "ok":
        return print(Color.GREEN + "[OK] " + Color.DEFAULT + str(msg))
    if status == "err":
        return print(Color.RED + "[ERROR] " + Color.DEFAULT + str(msg))
    if status == "warn":
        return print(Color.YELLOW + "[WARNING] " + Color.DEFAULT + str(msg))
    if status == "info":
        return print(Color.BLUE + "[INFO] " + Color.DEFAULT + str(msg))


def demo():
    """
    Demonstration
    """
    print(Color.GREEN + "[OK] " + Color.DEFAULT + "Hello World!")
    print(Color.RED + "[ERROR] " + Color.DEFAULT + "Hello World!")
    print(Color.YELLOW + "[WARNING] " + Color.DEFAULT + "Hello World!")
    print(Color.LBLUE + "[INFO] " + Color.DEFAULT + "Hello World!")
