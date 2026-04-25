# Globals.py

from Application.ConfigManager.ConfigManager import ConfigManager
from Application.ThemeManager.ThemesManager import ThemesManager

class AppContext:

    def __init__(self) -> None:
        
        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.loadSettings()

        # ThemeManager
        self.ThemeManager = ThemesManager()

ctx = AppContext()


