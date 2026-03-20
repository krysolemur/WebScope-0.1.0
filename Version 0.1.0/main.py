# main.py

# Importing system files
import sys
import signal
import os
import traceback


from PySide6.QtWidgets import QApplication # type: ignore
from PySide6.QtCore import QTimer # type: ignore


# Importing program files
from libs.Logging.logging import Logging
from libs.application import Application
from libs.Errors.exceptions import *
from Commands.commands import Commands


# Create signal for canceling (Ctrl + C)
# DEBUG
signal.signal(signal.SIGINT, signal.SIG_DFL)


'''
Class Main using Logging class as a parent for better logging into console and file. The Main class is start point of the application.
'''


# Main class
class Main(Logging):
    def __init__(self) -> None:
        # Init parents
        super().__init__()


        # Starting info message
        self.printf(msg="Starting WebScope", status="INFO")


        # Init application
        self.application = Application()


        # Execute applcation
        sys.exit(self.application.exec())


'''
Main block that is running and inicializing main class. Used too for running just some program with arguments in console
'''


# Main block
if __name__ == "__main__":
    # Try block for cathcing exceptions
    try:
        if len(sys.argv) == 2:
            # Save sys.argv[1] as command
            command = sys.argv[1]


            # Check if command exists
            if command not in Commands().commands:
                # Raise unknown command exception
                raise UnknownCommandError()
            

            # --run command for running application
            if command == "--run":
                # Creating insatence of Main class
                main = Main

                
                # Running main
                main()
        # Check parametres
        elif len(sys.argv) > 2:
            # Raise too many arguments exception
            raise TooManyArgumentsError()
        else:
            print("Run \"python3 main.py --run\" to start application.")
    except Exception as e:
        # Print exception
        traceback.print_exception(type(e), e, e.__traceback__)

