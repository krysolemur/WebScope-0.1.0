# stylesheet.py

# Import system modules

# Import program files
from noctua.style_manager import StyleCreator
from noctua.context import ctx

# Class stylesheet
class StyleManager:

    # Stylesheet dir
    styleDir = "resources/Stylesheets"
    
    # Initiator
    def __init__(self) -> None:

        # Save object to context
        ctx.StyleManager = self
        
        # None
        None
    
    # Create sheet
    @staticmethod
    def create_sheet() -> None:
        # Create instance
        styleCreator = StyleCreator()

        # Exec
        styleCreator.exec()