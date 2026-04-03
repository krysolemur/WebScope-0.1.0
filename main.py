# main.py


# Importing system files
import sys
import signal
import traceback


# Importing program files
from libs.application import Application
from libs.Commands.commands import Commands


# Create signal for canceling (Ctrl + C)
# DEBUG
signal.signal(signal.SIGINT, signal.SIG_DFL)


'''
Class Main using Logging class as a parent for better logging into console and file. The Main class is start point of the application.
'''


# Main class
class Main:
    def __init__(self) -> None:
        # Init parents
        super().__init__()


        # Init application
        self.application = Application()


        # Execute applcation
        sys.exit(self.application.exec())


'''
Main block that is running and inicializing main class. Used too for running just some program with arguments in console
'''


# Main block
if __name__ == "__main__":
    # Init commands
    commands = Commands()


    # Try block for cathcing exceptions
    try:
        '''
        Checking arguments and running commands.
        '''


        if len(sys.argv) == 2:
            # Save sys.argv[1] as command
            command = sys.argv[1]


            # Check if command exists
            if command not in commands.commands.keys():
                # Unknown command error
                print("Unknown command! Try --help for help menu.")


                # Exit
                sys.exit(1)
            

            # --run command for running application
            if command == "--run":
                # Creating insatence of Main class
                main = Main

                
                # Running main
                main()


            # Run others commands
            else:
                # Run command from command module
                commands.commands[command]()


        # Check parametres
        elif len(sys.argv) > 2:
            # Print too many arguments error
            print("Too many arguments used! Try --help for help menu.")


            # Exit
            sys.exit(1)
        

        else:
            # Print help command for running
            print("Run \"python3 main.py --run\" to start application. Type \"--help\" for help menu.")
            
    
    # Catch exception
    except Exception as e:
        # Print exception
        traceback.print_exception(type(e), e, e.__traceback__)

