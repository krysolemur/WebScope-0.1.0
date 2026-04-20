# configmanager.py

# Import system files
import json
import os

# Main class Config:
class ConfigManager:

    # Config file path
    configPath = "Config/config.json"

    # Default app configuration
    defaultConfig = {
        "GeneralPage": {
            "cb_gen_theme": "Light",
            "fcb_gen_font": "Noto Sans",
            "cb_gen_font_size": "Medium (recommended)",
            "sb_adv_autosave_interval": 5,
            "chk_adv_gpu": True,
            "cb_adv_startup": "Show Dashboard",
            "chk_sys_updates": True,
            "chk_sys_telemetry": False,
            "cb_sys_lang": "English"
        },
        "LoggingPage": {
            "cb_console_time": "Yes",
            "cb_console_colors": "Yes",
            "btn_console_info": True,
            "btn_console_warning": True,
            "btn_console_success": True,
            "btn_console_error": True,
            "btn_console_debug": True,
            "cb_file_enabled": "Yes",
            "btn_file_info": True,
            "btn_file_warning": True,
            "btn_file_success": True,
            "btn_file_error": True,
            "btn_file_debug": True,
            "sb_file_rotation": 10,
            "sb_file_retention": 7,
            "le_file_path": "./Logs",
            "cb_file_compression": "zip"
        },
        "SourcePage": {
            "elementsButton": {
                "color": "#569cd6",
                "background-color": "none",
                "font-weight": "bold",
                "font-style": "none",
                "text-decoration": "none",
                "transform": "none"
            },
            "atributsButton": {
                "color": "#9cdcfe",
                "background-color": "none",
                "font-weight": "none",
                "font-style": "none",
                "text-decoration": "none",
                "transform": "none"
            },
            "attrValuesButton": {
                "color": "#ce9178",
                "background-color": "none",
                "font-weight": "none",
                "font-style": "none",
                "text-decoration": "none",
                "transform": "none"
            },
            "stringButton": {
                "color": "#ce9178",
                "background-color": "none",
                "font-weight": "none",
                "font-style": "none",
                "text-decoration": "none",
                "transform": "none"
            },
            "commentsButton": {
                "color": "#6a9955",
                "background-color": "none",
                "font-weight": "none",
                "font-style": "italic",
                "text-decoration": "none",
                "transform": "none"
            }
        }
    }

    # Initiator
    def __init__(self) -> None:

        # Init parents
        super().__init__()
        
        # Check default config file
        self._checkConfiguration()

    '''
    Private functions.
    '''
    
    # Check if configuration file config.json exists. If does not, create it with default settings.
    def _checkConfiguration(self) -> None:
        # Check Config/config.json in main directory
        if not os.path.exists(self.configPath):

            # Create general.json
            with open(self.configPath, "w") as config:
                # Write default settings
                json.dump(self.defaultConfig, config, indent=4)

                # Close file
                config.close()

    '''
    Public functions.
    '''

    # Load settings from disk and parse it. If parsing fail, use default settings.
    def loadSettings(self) -> dict:
        # Try except
        try:
            # Open file
            with open(self.configPath, "r") as config:
                # Parsing json
                return json.load(config)
        except FileNotFoundError as e:
            # Return default config
            return self.defaultConfig
        except json.decoder.JSONDecodeError as e:
            # Return default
            return self.defaultConfig

    # Public version of save settings function that is used in settings dialog which is calling from.
    def saveSettings(self, settings) -> None:
        # Open profile
        with open(self.configPath, "w") as nwconfig:
            # Write into profile new configuration
            json.dump(settings, nwconfig, indent=4)
        
    # Public function used in settings dialog for overwriting config file with default json config.
    def resetSettings(self) -> None:
        # Open profile
        with open(self.configPath, "w") as nwconfig:
            # Write into profile new configuration
            json.dump(self.defaultConfig, nwconfig, indent=4)

