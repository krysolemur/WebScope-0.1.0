# commands.py

# Import system files
import sys

# Importing program files
from Config.configmanager import ConfigManager
from libs.MainWindow.mainwindow import MainWindow

# Stored all commands 

# Class commands 
class Commands:
    def __init__(self):
        # List of all existing command for WebScope application and their function
        self.commands = {
            "--run": None,
            "--help": self.help,
            "--reset-settings": ConfigManager().resetSettings,
            "--create-settings": ConfigManager()._checkConfigFile,
        }
        
        # List of all commands and their description
        self.commandsList = {
            "--run": "Run application.",
            "--help": "Show commands menu iwth description for each command.",
            "--reset-settings": "Reset settings in Config/config.json",
            "--create-settings": "Create new settings if previous was deleted or renamed."
        }
        
    '''
    Commands.
    '''
    
    # Help function that shows all comands and their descriptions.
    def help(self) -> None:
        # Browse all commands
        for command, description in self.commandsList.items():
            # Print command
            print(f"{command:<{len(max(list(self.commandsList.keys()), key=len))}} -> {description}")



