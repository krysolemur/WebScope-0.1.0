# Globals.py

from Application.ConfigManager.ConfigManager import ConfigManager
from Application.ThemeManager.ThemesManager import ThemesManager
from Application.StyleManager.StyleManager import StyleManager

class AppContext:

    def __init__(self) -> None:
        
        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.load_settings()
        
        # ThemeManager
        self.ThemesManager = ThemesManager()

        # StyleManager
        self.StyleManager = StyleManager()

ctx = AppContext()


