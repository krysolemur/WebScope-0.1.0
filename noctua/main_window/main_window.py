# MainWindow.py

import requests
import jsbeautifier # type: ignore

from PySide6.QtWidgets import QDialog, QApplication, QMainWindow # type: ignore

from noctua.settings_dialog import SettingsDialog
from noctua.ui_gen import Ui_MainWindow
from noctua.core.context import ctx

class MainWindow(QMainWindow):

    def __init__(self) -> None:

        super().__init__()

        # Load Ui
        self.ui = Ui_MainWindow()

        # Setup Ui
        self.ui.setupUi(self)

        # Quit application
        self.ui.actionQuit.triggered.connect(ctx.app.quit_application)

        # # Restart application
        self.ui.actionRestart.triggered.connect(ctx.app.restart_application)

        # Open settings dialog
        self.ui.actionSettings.triggered.connect(self._open_settings)

        # Open about dialog
        self.ui.actionAbout.triggered.connect(self._about_dialog)

        # Theme creator
        self.ui.actionThemeCreator.triggered.connect(self._open_theme_creator)

        # Style creator
        self.ui.actionStylesheetCreator.triggered.connect(self._open_style_creator)

        # Set window title
        self.setWindowTitle(f"{ctx.app.NAME} | {ctx.app.VERSION}")  

        # Resize to default size
        self.resize(800, 600) 

        # Center main window
        self._center_window(self)

    # Show app information
    def _about_dialog(self) -> None:
        # Import about dialog
        from noctua.ui_gen.about_dialog import Ui_AboutDialog
        
        # Create dialog
        aboutDialog = QDialog(self)

        # Load Ui
        aboutDialogUi = Ui_AboutDialog()

        # Set Ui
        aboutDialogUi.setupUi(aboutDialog)

        # Set title 
        aboutDialog.setWindowTitle(f"{self.app.NAME} | {self.app.VERSION} | About")  

        # Adjust size for dialog
        aboutDialog.resize(aboutDialog.sizeHint())

        # Set version text to label 
        aboutDialogUi.versionLabel.setText(f"{aboutDialogUi.versionLabel.text()} {self.app.VERSION}")

        # Show dialog
        aboutDialog.show()

        # Setn GET request
        source = requests.get(self.url)
        
        # Check if page is loaded 
        source.raise_for_status()

        # Set parametres for formating
        opts = jsbeautifier.default_options()

        # Ident size four spaces
        opts.indent_size = 4  

        # Long rows
        opts.wrap_line_length = 80  
        
        # Format whole text (HTML, CSS, JS)
        formatted_code = jsbeautifier.beautify(source.text, opts)
        
        # Return formated source code for better reading
        return formatted_code

    # Center window/dialog
    @staticmethod
    def _center_window(window) -> None:
        # Get screen size
        screen = QApplication.primaryScreen()

        # Get geometry
        screen_geometry = screen.geometry()

        # Count half of creen
        x = (screen_geometry.width() - window.width()) // 2
        y = (screen_geometry.height() - window.height()) // 2

        # Move to center
        window.move(x, y)

    # Open settings dialog
    @staticmethod
    def _open_settings() -> None:
        # Open and exec settings dialog
        settingsDialog = SettingsDialog()
        settingsDialog.exec()

    # Open theme creator
    @staticmethod
    def _open_theme_creator() -> None:
        # Open dialog
        ctx.theme_manager.create_theme()
    
    # Open style creator
    @staticmethod
    def _open_style_creator() -> None:
        # Open dialog
        ctx.style_manager.create_sheet()
    
    # Close event overwritten.
    @staticmethod
    def closeEvent() -> None:
        # Quit application
        ctx.logger.info("Closing main window.")
        ctx.app.quit_application()