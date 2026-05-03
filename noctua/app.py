# Application.py

import os
import sys

from PySide6.QtWidgets import QApplication # type: ignore
from PySide6.QtGui import QFont # type: ignore

from noctua.main_window import MainWindow
from noctua.theme_manager import ThemeManager
from noctua.style_manager import StyleManager
from noctua.context import ctx

class Noctua(QApplication):

    # Version 
    VERSION = "0.1.0"

    # Application name
    NAME = "XyraEngine"
    
    # Icon path
    ICON_PATH = ""

    def __init__(self) -> None:
        
        # Init parents
        super().__init__(sys.argv)

        # Save app, theme manager and style manager to context
        ctx.app = self
        ctx.theme_manager = ThemeManager()
        ctx.style_manager = StyleManager()

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
        new_config = ctx.ConfigManager.load_settings()

        # Clear config
        ctx.config.clear()

        # Update
        ctx.config.update(new_config)

    # Restart application function
    def restart_application(self) -> None:
        # Restart command
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Quit application
    def quit_application(self) -> None:
        # Quit
        QApplication.quit()