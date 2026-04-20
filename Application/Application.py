# Application.py

# Import system files
import os
import sys

from PySide6.QtWidgets import QApplication, QDialog # type: ignore
from PySide6.QtGui import QFont # type: ignore

# Importing program files
from Application.ConfigManager.ConfigManager import ConfigManager
from Application.ThemeManager.ThemesManager import ThemesManager
from Application.MainWindow.MainWindow import MainWindow
from Application.Logger.Logger import Logger

# Class for managing whole application
class Application(QApplication):

    # Version 
    version = "0.1.0"

    # Application name
    name = "XyraEngine"
    
    # Icon path
    icon_path = ""

    # Initiator
    def __init__(self) -> None:
        
        # Init parents
        super().__init__()

        # Config object
        self.ConfigManager = ConfigManager()

        # Config variable
        self.config = self.ConfigManager.loadSettings()

        # Logger object
        self.Logger = Logger(self.config["LoggingPage"], self.name)

        # ThemeManager
        self.ThemesManager = ThemesManager()

        # Setup application
        self._setup_application()

        # Init MainWindow
        self.MainWindow = MainWindow(self)

        # Show main window
        self.MainWindow.show()

    # Setup function that loads general settings
    def _setup_application(self) -> None:
        # Get configuration
        config = self.config["GeneralPage"]

        # Font size dictonary
        font_size = {
            "Large": 12,
            "Medium (recommended)": 10,
            "Small": 8
        }

        # Set font and font size for whole application
        self.setFont(QFont(str(config["fcb_gen_font"]), int(font_size[str(config["cb_gen_font_size"])])))

    # Reload config
    def reload_config(self) -> None:
        # New config variable
        new_config = self.ConfigManager.loadSettings()

        # Clear config
        self.config.clear()

        # Update
        self.config.update(new_config)

    # Restart application function
    def restart_application(self) -> None:
        # Restart command
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Quit application
    def quit_application(self) -> None:
        # Quit
        QApplication.quit()