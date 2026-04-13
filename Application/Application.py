# Application.py

# Import system files
import os
import sys

from PySide6.QtWidgets import QApplication # type: ignore
from PySide6.QtGui import QFont # type: ignore

# Importing program files
from Application.MainWindow.MainWindow import MainWindow

from Logs.Logger import Logger

from Config.ConfigManager import ConfigManager

# Class for managing whole application
class Application(QApplication):

    # Version 
    version = "0.1.0"

    # Application name
    name = "XyraEngine"
    
    # Icon path
    iconPath = ""

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

        # Setup application
        self._setupApplication()

        # Init MainWindow
        self.MainWindow = MainWindow(self)

        # Show main window
        self.MainWindow.show()
        
    '''
    Private functions.
    '''

    # Setup function that loads general settings
    def _setupApplication(self) -> None:
        # Get configuration
        config = self.ConfigManager.config["GeneralPage"]

        # Font size dictonary
        fontSize = {
            "Large": 12,
            "Medium (recommended)": 10,
            "Small": 8
        }

        # Set font and font size for whole application
        self.setFont(QFont(str(config["fontComboBox"]), int(fontSize[str(config["fontSizeComboBox"])])))

    '''
    Public functions.
    '''

    # Reload config
    def reloadConfiguration(self) -> None:
        # New config variable
        self.config = self.ConfigManager.loadSettings()

    # Restart application function
    def restartApplication(self) -> None:
        # Restart command
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Quit application
    def quitApplication(self) -> None:
        # Quit
        QApplication.quit()