from noctua.config_manager import ConfigManager

class Context:

    def __init__(self) -> None:

        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.load_settings()
        
ctx = Context()


