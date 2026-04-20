# stylesheet.py

# Import system modules
import shutil

# Class stylesheet
class StyleManager:

    # Stylesheet dir
    styleDir = "resources/Stylesheets"
    
    # Initiator
    def __init__(self) -> None:

        # None
        None
    
    # TODO: Move file to theme dir
    @classmethod
    def addTheme(cls, path) -> bool:
        try:
            # Move that file to themes dir
            shutil.move(path, cls.styleDir)

            return True
        except Exception as e:
            print(e)
            return False