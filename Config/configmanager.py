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
        self.default_config = {
            "askOnCloseComboBox": "Yes",
            "themeComboBox": "",
            "fontComboBox": "Ubuntu",
            "fontSizeSlider": 0,
            "checkUpdatesComboBox": "Yes"
        }

        # General config 
        self.general_config = {}

        # Config folder path
        self.config_dir = "Config"

        # Config file path
        self.default_path = "Config/config.json"

        # General config path
        self.general_path = "Config/general.json"

        # Check default config file
        self.checkDefaultConfig()

        # Check general config file
        self.checkGeneralConfig()

        # Configuration variable
        self.config = self._loadSettings

        # Load settings 
        self.config()

    '''
    Private functions.
    '''

    # Load settings from disk
    def _loadSettings(self) -> list:
        # Settings list
        settings = {}

        # Try except
        try:
            # Open file
            with open(f"{self.config_dir}/config.json", "r") as config:
                # Parsing json
                return json.load(config)
        except FileNotFoundError as e:
            # Error msg
            self.printe(msg=f"Configuration file not found, applaying default config", function=self._loadSettings.__name__, exception=e)

            # Return default config
            return self.default_config
        except json.decoder.JSONDecodeError as e:
            # Show message
            self.printe(msg=f"Error while parsing config.json, applying default config", exception=e, function=self._loadSettings.__name__)

            # Return default
            return self.default_config
    
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

    # Check general config file
    def checkGeneralConfig(self) -> None:
        # Check Config/general.json in config directory
        if not os.path.exists(self.general_path):
            # Print warning
            self.printw(msg=f"General config doesen't exists! Creating new.")

            # Create general.json
            with open(self.general_path, "w") as config:
                # Write default settings
                json.dump(self.general_config, config, indent=4)

                # Close file
                config.close()

    '''
    Settings methods.
    '''

    # Save settings 
    def saveSettings(self, settings) -> None:
        # Open profile
        with open(f"{self.config_dir}/config.json", "w") as nwconfig:
            # Write into profile new configuration
            json.dump(settings, nwconfig, indent=4)

        # Print saved
        self.printo(msg="Settings saved")
        
    # Reset settings
    def resetSettings(self) -> None:
        # Open profile
        with open(f"{self.config_dir}/config.json", "w") as nwconfig:
            # Write into profile new configuration
            json.dump(self.default_config, nwconfig, indent=4)
        
        # Log message
        self.printi(msg="Settings reseted")

    