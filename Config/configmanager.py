# configmanager.py

# Import system files
import json
import sys
import os
import re

# Import program files
from libs.Logging.logging import Logging

# Main class Config:
class ConfigManager(Logging):
    def __init__(self):
        '''
        Init parents, set variables and setup config manager.
        '''
        # Init parents
        super().__init__()

        # Default app config
        self.default_config = {}

        # Config folder path
        self.config_dir = "Config"

        # Config file path
        self.default_path = "Config/config.json"

        # All profiles
        self.all_profiles = self._getProfiles

        # Check default config file
        self.checkDefaultConfig()


    '''
    Private functions.
    '''

    # Get all profiles
    def _getProfiles(self) -> list:
        # Create list
        profiles = []

        # List config directory
        for config in os.listdir(self.config_dir):
            # Check json type
            if config.endswith(".json"):
                # Append config to profiles
                profiles.append(config)

        # Return list
        return profiles
    
    '''
    Public functions.
    '''

    # Check default config file
    def checkDefaultConfig(self) -> None:
        # Check Config/config.json in main directory
        if not os.path.exists(self.default_path):
            # Print warning
            self.printw(msg=f"Default config doesen't exists! Creating new.")

            # Create general.json
            with open(self.default_path, "w") as config:
                # Write default settings
                json.dump(self.default_config, config, indent=4)

                # Close file
                config.close()

    '''
    Profiles methods.
    '''

    # Add profile function
    def addProfile(self, name) -> None:
        # Create config file
        with open(f"{self.config_dir}/{name}.json", "w") as nwconfig:
            # Write json
            json.dump(self.default_config, nwconfig, indent=4)

    # Remove profile function
    def removeProfile(self, name) -> None:
        # Try remove profile
        os.remove(f"{self.config_dir}/{name}")

    '''
    Settings methods.
    '''

    # Save settings 
    def saveSettings(self, profile) -> None:
        new_config = 0
        # Open profile
        with open(f"{self.config_dir}/{profile}", "w") as nwconfig:
            # Write into profile new configuration
            json.dump(new_config, nwconfig, indent=4)
        
    # Reset settings
    def resetSettings(self, profile) -> None:
        # Open profile
        with open(f"{self.config_dir}/{profile}", "w") as nwconfig:
            # Write into profile new configuration
            json.dump(self.default_config, nwconfig, indent=4)

    # Load settings from disk
    def loadSettings(self, profile) -> None:
        None
    