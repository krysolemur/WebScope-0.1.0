# theme.py

# Importing system files
import shutil

# Import program files
from Application.ThemeManager.ThemeCreator import ThemeCreator

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
    def addTheme(cls, path) -> bool:
        try:
            # Move that file to themes dir
            shutil.move(path, cls.themeDir)

            return True
        except Exception as e:
            print(e)
            return False

    # Theme creator
    @staticmethod
    def create_theme() -> None:
        # Init main theme creator class
        themeCreator = ThemeCreator()

        # Execute the class
        themeCreator.exec()

    