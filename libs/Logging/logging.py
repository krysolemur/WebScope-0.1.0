# logging.py

# Importing
import traceback
import sys

# This python file will be using for logging into files if enabled

# Main class Logging 
class Logging:
    def __init__(self, *args, **kwargs) -> None:
        # Init arguments
        super().__init__(*args, **kwargs)

        # Accept types terminal
        self.accept_types_terminal = []

        # Accept types file
        self.accept_types_file = {

        }

    # Print error
    def printe(self, exception, function, endch=".\n", msg=None, ) -> None:
        # Get info from error
        exc_type, exc_value, exc_tb = sys.exc_info()
        last_tb = traceback.extract_tb(exc_tb)[-1]

        # Print error    
        print(f"[  \033[31mERROR\033[0m   ] {msg if msg else "ERROR"} at line {last_tb.lineno} in {last_tb.filename} in {function}", end=endch)

        print(exception)

    # Print info
    def printi(self, msg, endch=".\n") -> None:
        # Print info
        print(f"[   \033[96mINFO\033[0m   ] {msg}", end=endch)

    # Print OK
    def printo(self, msg=None, function=None, endch=".\n") -> None:
        # Print ok
        print(f"[    \033[92mOK\033[0m    ] {msg if msg else f"{function} run successfully"}", end=endch)

    # Print warning
    def printw(self, msg, endch=".\n") -> None:
        # Print warning
        print(f"[  \033[33mWARNING\033[0m ] {msg}", end=endch)

    # Print critical
    def printc(self, msg=None, endch=".\n") -> None:
        # Print info
        print(f"[ \033[1m\033[31mCRITICAL\033[0m ] {msg + "! " if msg else ""}Exiting program", end=endch)

        # Exit program
        sys.exit(1)

    # Print debug
    def printd(self, msg, endch=".\n") -> None:
        # Print debug
        print(f"[  \033[95mDEBUGS\033[0m  ] {msg}", end=endch)