# Commands.py

# Import system files
import sys

# Importing program files
from Application.ConfigManager.ConfigManager import ConfigManager

from Application.Application import Application as app

from Application.ThemeManager.ThemeCreator import ThemeCreator

from Application.Logger.Logger import Logger

# Stored all commands 

# Class commands 
class Commands:
    
    # Initiator
    def __init__(self):

        # Command name
        self.commandName = "./main"

        # All commands without --
        self.allCommands = ["run", "help", "reset-settings", "create-settings", "version"]
        
        # List of all existing command for WebScope application and their function
        self.commands = {
            "--run": None,
            "--help": self._help,
            "--reset-settings": self._resetSettings,
            "--create-settings": self._createSettings,
            "--version": self._version,
            "--create-theme": self._createTheme,
            "--clear-logs": self._clearLogs
        }
        
        # List of all commands and their description
        self.commandsDescriptions = {
            "--run": "Run application.",
            "--help": "Display help message.",
            "--reset-settings": "Reset program configuration.",
            "--create-settings": "Create new settings if previous was deleted or renamed.",
            "--version": "Show actual version of application.",
            "--create-theme": "Show dialog for creating own theme.",
            "--clear-logs": "Clear all logs."
        }

        # List of all arguments assigned to each function
        self.commandsArguments = {
            "--run": None,
            "--help": "<command>",
            "--reset-settings": None,
            "--version": None,
            "--create-settings": None,
            "--create-theme": None,
            "--clear-logs": None
        }

    '''
    Commands.
    '''
    
    # Help function that shows all comands and their descriptions.
    def _help(self, *args) -> None:
        # Get command
        cmd = str(*args[0])

        # If there is not command
        if not cmd:
            # Browse all commands
            for command, description in self.commandsDescriptions.items():
                # Print command
                print(f"{command:<{len(max(list(self.commandsDescriptions.keys()), key=len))}} {description}")
        else:
            # Check if command even exists
            if cmd not in self.allCommands:
                # Show unknown command
                print("Unknown argument used! Try --help for help menu.")

                # Exit script
                sys.exit(1)

            # Print usage for that one command
            print(f"Usage: {cmd} {[arg for arg in self.commandsArguments.values()]}")

    # Version function
    def _version(self, *args) -> None:
        # Print actual version
        print(f"{app.name} version {app.version}")

    # Reset settings function
    def _resetSettings(self, *args) -> None:
        # Reset settings
        ConfigManager().resetSettings()

    # Create configuration
    def _createSettings(self, *args) -> None:
        # Create settings file
        ConfigManager()._checkConfigFile()

    # TODO: Create theme
    def _createTheme(self, *args) -> None:
        # Init theme creator
        ThemeCreator().exec()

    # Clear logs
    def _clearLogs(self) -> None:
        # Clear
        Logger.clearLogs()