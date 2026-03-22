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

# Unknown command
class UnknownCommandError(Exception):
    def __init__(self, msg=None):
        # Check message
        print(msg) if msg else print("Unknown command! Try --help for help menu.")

        # Exit program
        sys.exit(1)

# Wrong password exception
class LoginError(Exception):
    def __init__(self, user, msg=None):
        # Print msg if there is any msg
        print(msg) if msg else print(f"Wrong password for user {user}!")

        # Exit
        sys.exit(1)