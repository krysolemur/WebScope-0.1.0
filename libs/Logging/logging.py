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
    def printe(self, exception=None, function=None, endch=".\n", msg=None) -> None:
        # Get info from error
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb_list = traceback.extract_tb(exc_tb)
        
        # Check tb_lsit
        if tb_list:
            # Get index
            last_tb = tb_list[-1]
        else:
            # Else None
            last_tb = None

        # Print error    
        print(f"[  \033[31mERROR\033[0m   ] {msg if msg else "ERROR"}{f"at line {last_tb.lineno} in {last_tb.filename}" if exception else ""}{f" in {function}" if function else ""}", end=endch)

        print(exception) if exception else None

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

    # Print login error
    def printl(self, msg, endch=".\n") -> None:
        print(f"[  \033[31mERROR\033[0m   ] {msg}", end=endch)