"""This module contains everything related to printing colored things."""

# pylint: disable-next=too-few-public-methods
class BColors:
    """
    Colors from the blender build script.
    See: https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_colored(text: str, color: str):
    print(f"{color}{text}{BColors.ENDC}")
