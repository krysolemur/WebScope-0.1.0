# exceptions.py

# This is for calling exceptions and user errors, into terminal or in window if enabled

# Importing system files
import sys

# Too many arguments exception
class TooManyArgumentsError(Exception):
    def __init__(self, msg=None) -> None:
        # Check message
        print(msg) if msg else print("Too many arguments used! Try --help for help menu.")

        # Exit program
        sys.exit(1)
