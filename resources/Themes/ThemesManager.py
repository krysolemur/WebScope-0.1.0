# theme.py

# Importing system files
import shutil
import json
import os

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox # type: ignore
from PySide6.QtGui import QPalette, QColor # type: ignore
from PySide6.QtCore import Qt # type: ignore

# Import program files
from resources.Themes.ThemeCreator import ThemeCreator

# Main class ThemeManager
class ThemesManager:

    # Themes dir
    themeDir = "resources/Themes"

    # Initiator
    def __init__(self) -> None:

        # Init parents
        super().__init__()

        # Themes mapping
        self.defaultThemes = {
            "Dark": lambda: self.loadPalette("Dark"),
            "Light": lambda: self.loadPalette("Light")
        }

    # Move file to theme dir
    def addTheme(self, path) -> bool:
        try:
            # Move that file to themes dir
            shutil.move(path, cls.themeDir)

            return True
        except Exception as e:
            print(e)
            return False

    # Theme creator
    def createTheme(self) -> None:
        # Init main theme creator class
        themeCreator = ThemeCreator()

        # Execute the class
        themeCreator.exec()

    