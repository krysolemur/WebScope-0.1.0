# main.py

'''
Importing system files for process management, signal handling, 
and detailed error tracking.
'''

# Standard library for system-specific parameters and functions
import sys

# Module to set handlers for asynchronous events (e.g., keyboard interrupts)
import signal

# Module for extracting, formatting and printing stack traces of Python programs
import traceback


'''
Importing program-specific modules for the main application logic 
and command-line interface handling.
'''

# The core Application class that manages the GUI and main loop
from libs.application import Application

# Module containing the definitions for supported console commands
from libs.Commands.commands import Commands


# Set the signal handler for Interrupt (Ctrl+C) to the default behavior
signal.signal(signal.SIGINT, signal.SIG_DFL)


'''
The Main class serves as the entry point for the graphical version of the application.
It initializes the application logic and starts the event loop.
'''

# Define the Main class as the starting point
class Main:

    # Constructor method for the Main class
    def __init__(self) -> None:

        # Initialize any parent classes if they exist (using super)
        super().__init__()


        # Create an instance of the core Application class
        self.application = Application()


        # Execute the application and exit the script with its return code
        sys.exit(self.application.exec())


'''
Main execution block. This part handles command-line arguments,
initializes the command logic, and catches global exceptions.
'''

# Check if the script is being run directly as the main module
if __name__ == "__main__":

    # Initialize the command management class
    commands = Commands()


    # Try block to wrap the execution for global error handling
    try:

        '''
        Argument handling logic: determines whether to run the GUI 
        or a specific console command.
        '''


        # Check if exactly one command-line argument was provided
        if len(sys.argv) == 2:

            # Store the first argument (index 1) into a command variable
            command = sys.argv[1]


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

                # Execute the function associated with the command key
                commands.commands[command]()


        # Check if the user provided more than the expected number of arguments
        elif len(sys.argv) > 2:

            # Print an error message regarding excessive arguments
            print("Too many arguments used! Try --help for help menu.")


            # Exit the script with an error status code
            sys.exit(1)
        

        # Handle the case where no arguments were provided at all
        else:

            # Provide the user with instructions on how to start the application
            print("Run \"python3 main.py --run\" to start application. Type \"--help\" for help menu.")
            
    
    # Generic catch-all for any exceptions that occur during runtime
    except Exception as e:

        # Print a full traceback of the exception for debugging purposes
        traceback.print_exception(type(e), e, e.__traceback__)