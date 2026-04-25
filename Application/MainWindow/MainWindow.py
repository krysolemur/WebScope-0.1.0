# MainWindow.py

# Importing system files
import requests
import jsbeautifier # type: ignore

from PySide6.QtWidgets import QDialog, QApplication, QMainWindow # type: ignore

# Imporing program files
from Application.SettingsDialog.SettingsDialog import SettingsDialog

from Application.QtFiles.MainWindow import Ui_MainWindow
from Application.QtFiles.AboutDialog import Ui_aboutDialog

from Application.AppContext import ctx

# MainWindow class
class MainWindow(QMainWindow):

    # Constructor
    def __init__(self) -> None:

        # Init parents
        super().__init__()

        # ThemesManager
        self.ThemesManager = ctx.ThemesManager

        # StyleManager
        self.StyleManager = ctx.StyleManager

        # Load Ui
        self.ui = Ui_MainWindow()

        # Setup Ui
        self.ui.setupUi(self)

        # Quit application
        self.ui.actionQuit.triggered.connect(ctx.app.quit_application)

        # Restart application
        self.ui.actionRestart.triggered.connect(ctx.app.restart_application)

        # Open settings dialog
        self.ui.actionSettings.triggered.connect(self._open_settings)

        # Open about dialog
        self.ui.actionAbout.triggered.connect(self._about_dialog)

        # Open target dialog
        self.ui.actionSetTarget.triggered.connect(self._setTargetAction)

        # Theme creator
        self.ui.actionThemeCreator.triggered.connect(self._open_theme_creator)

        # Style creator
        self.ui.actionStylesheetCreator.triggered.connect(self._open_style_creator)

        # Set window title
        self.setWindowTitle(f"{ctx.app.NAME} | {ctx.app.VERSION}")  

        # Set window icon

        # Resize to default size
        self.resize(800, 600) 

        # Center main window
        self._center_window(self)

    # Center window/dialog
    def _center_window(self, window) -> None:
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
    def _open_settings(self) -> None:
        # Create settings dialog object
        self.SettingsDialog = SettingsDialog()

        # Exec settings dialog
        self.SettingsDialog.exec()

    # TODO: Set target 
    def _setTargetAction(self) -> None:
        None

    # Open theme creator
    def _open_theme_creator(self) -> None:
        # Open dialog
        self.ThemesManager.create_theme()
    
    # Open style creator
    def _open_style_creator(self) -> None:
        # Open dialog
        self.StyleManager.create_sheet()

    # Show software information
    def _about_dialog(self) -> None:
        # Create dialog
        aboutDialog = QDialog(self)

        # Load Ui
        aboutDialogUi = Ui_aboutDialog()

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
    
    # Close event overwritten.
    def closeEvent(self, event) -> None:
        # Quit application
        QApplication.quit()