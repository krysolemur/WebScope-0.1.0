# main.py

# Importing system files
import sys
import signal
import traceback

# Importing program files
from Application.Application import Application

from Application.Commands.Commands import Commands

# Set the signal handler for Interrupt (Ctrl+C) to the default behavior
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Createing Main class as program starter
class Main:

    # Constructor for the Main class
    def __init__(self) -> None:

        # Application object
        self.Application = Application()

        # Exit program with return code
        sys.exit(self.Application.exec())

# Run script only as interpreter, not as module
if __name__ == "__main__":

    # Init command class
    commands = Commands()

    # Try block for catching errors
    try:

        # Check if exactly one command-line argument was provided
        if len(sys.argv) > 1:

            # Store the first argument (index 1) into a command variable
            command = sys.argv[1]

            # Store others arguments from index 2
            arguments = sys.argv[2::]

            # Verify if the provided command exists in the defined commands dictionary
            if command not in commands.commands.keys():

                # Inform the user about the invalid command
                print("Unknown command! Try --help for help menu.")

                # Exit the script with an error status code
                sys.exit(1)
        
            # Check if the specific command is the trigger to run the GUI
            if command == "--run":

                # Assign the Main class to a variable for instantiation
                main = Main
                
                # Create the Main instance, starting the application
                main()

            # Handle all other valid commands defined in the commands module
            else:

                # Try block for cathing too many argument error
                try:

                    # Run command
                    commands.commands[command](arguments)

                except TypeError:

                    # Print missing argument error
                    print(f"{command}: Missing command operands")
                
                    # Print help command
                    print(f"Try --help {command[2::] + " " if command != "--help" else ""}for more information.")

        # Handle the case where no arguments were provided at all
        else:

            # Provide the user with instructions on how to start the application
            print("Run \"python3 main.py --run\" to start application. Type \"--help\" for help menu.")
            
    # Generic catch-all for any exceptions that occur during runtime
    except Exception as e:

        # Print a full traceback of the exception for debugging purposes
        traceback.print_exception(type(e), e, e.__traceback__)