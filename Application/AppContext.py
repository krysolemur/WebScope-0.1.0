# Globals.py

from Application.ConfigManager.ConfigManager import ConfigManager

class AppContext:

    def __init__(self) -> None:
        
        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.loadSettings()

ctx = AppContext()


