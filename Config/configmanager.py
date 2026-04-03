# configmanager.py

# Import system files
import json
import os

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
        self.defaultConfig = {
            "askOnCloseComboBox": "No",
            "themeComboBox": "Light",
            "stylesheetComboBox": "",
            "fontComboBox": "Sans Serif",
            "fontSizeSlider": 10,
            "checkUpdatesComboBox": "No",
            "htmlElementsCheckBox": True,
            "htmlAtributsCheckBox": True,
            "atributsValuesCheckBox": True
        }
        # Config file path
        self.configPath = "Config/config.json"

        # Check default config file
        self._checkConfigFile()

        # Configuration variable
        self.configuration = self._loadSettings()

    '''
    Private functions.
    '''

    # Load settings from disk and parse it. If parsing fail, use default settings.
    def _loadSettings(self) -> list:
        # Settings list
        settings = {}

        # Try except
        try:
            # Open file
            with open(self.configPath, "r") as config:
                # Parsing json
                return json.load(config)
        except FileNotFoundError as e:
            # Error msg
            self.printe(msg=f"Configuration file not found, applaying default config", function=self._loadSettings.__name__, exception=e)

            # Return default config
            return self.defaultConfig
        except json.decoder.JSONDecodeError as e:
            # Show message
            self.printe(msg=f"Error while parsing config.json, applying default config", exception=e, function=self._loadSettings.__name__)

            # Return default
            return self.defaultConfig
    
    # Check if configuration file config.json exists. If does not, create it with default settings.
    def _checkConfigFile(self) -> None:
        # Check Config/config.json in main directory
        if not os.path.exists(self.configPath):
            # Print warning
            self.printw(msg=f"Default config doesen't exists! Creating new.")

            # Create general.json
            with open(self.configPath, "w") as config:
                # Write default settings
                json.dump(self.defaultConfig, config, indent=4)

                # Close file
                config.close()

    '''
    Public functions.
    '''

    # Public version of save settings function that is used in settings dialog which is calling from.
    def saveSettings(self, settings) -> None:
        # Open profile
        with open(self.configPath, "w") as nwconfig:
            # Write into profile new configuration
            json.dump(settings, nwconfig, indent=4)

        # Print that settings was saved
        self.printo(msg="Settings saved")
        
    # Public function used in settings dialog for overwriting config file with default json config.
    def resetSettings(self) -> None:
        # Open profile
        with open(self.configPath, "w") as nwconfig:
            # Write into profile new configuration
            json.dump(self.defaultConfig, nwconfig, indent=4)
        
        # Log message
        self.printi(msg="Settings reseted")

    