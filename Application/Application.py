# Application.py

import os
import sys

from PySide6.QtWidgets import QApplication # type: ignore
from PySide6.QtGui import QFont # type: ignore

from Application.MainWindow.MainWindow import MainWindow
from Application.Logger.Logger import logger

from Application.AppContext import ctx

class Application(QApplication):

    # Version 
    VERSION = "0.1.0"

    # Application name
    NAME = "XyraEngine"
    
    # Icon path
    ICON_PATH = ""

    def __init__(self) -> None:
        
        # Init parents
        super().__init__(sys.argv)

        # Save app
        ctx.app = self

        # Setup application
        self._setup_application()

        # Init MainWindow
        self.MainWindow = MainWindow()

        # Show main window
        self.MainWindow.show()

    # Setup function that loads general settings
    def _setup_application(self) -> None:
        # App name
        self.setApplicationName(self.NAME)

        config = ctx.config.get("GeneralPage", "")

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
        new_config = ctx.ConfigManager.loadSettings()

        # Clear config
        ctx.config.clear()

        # Update
        ctx.config.update(new_config)

    # Restart application function
    def restart_application(self) -> None:
        # Restart command
        logger.info("Restarting application.")
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Quit application
    def quit_application(self) -> None:
        # Quit
        logger.info("Quiting application.")
        QApplication.quit()