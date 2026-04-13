# MainWindow.py

# Importing system files
import requests
import jsbeautifier # type: ignore

from PySide6.QtWidgets import QDialog, QApplication, QMainWindow # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Imporing program files
from Application.SettingsDialog.SettingsDialog import SettingsDialog

from Application.QtFiles.MainWindow import Ui_MainWindow
from Application.QtFiles.AboutDialog import Ui_aboutDialog
from Application.QtFiles.TargetDialog import Ui_TargetDialog

# Main class window for managing window and loading GUI
class MainWindow(QMainWindow):

    # Initiator
    def __init__(self, app) -> None:

        '''
        Init parents and save instances.
        '''

        # Init parents
        super().__init__()

        # App variable
        self.app = app

        # ConfigManager
        self.ConfigManager = app.ConfigManager

        '''
        Load Ui for MainWindow.
        '''

        # Load Ui
        self.ui = Ui_MainWindow()

        # Setup Ui
        self.ui.setupUi(self)

        '''
        Add all actions for tool bar buttons.
        '''

        # Quit application
        self.ui.actionQuit.triggered.connect(self.app.quitApplication)

        # Restart application
        self.ui.actionRestart.triggered.connect(self.app.restartApplication)

        # Open settings dialog
        self.ui.actionSettings.triggered.connect(self._openSettingsAction)

        # Open about dialog
        self.ui.actionAbout.triggered.connect(self._aboutAction)

        # Open target dialog
        self.ui.actionSetTarget.triggered.connect(self._setTargetAction)

        '''
        Set window preferences.
        '''

        # Set window title
        self.setWindowTitle(f"{self.app.name} | {self.app.version}")  

        # Set window icon
        self.setWindowIcon(QIcon(self.app.iconPath))

        # Resize to default size
        self.resize(800, 600) 

        # Center main window
        self._centerWindow(self)

    '''
    Private functions.
    '''

    # Center function that center specific window which is given as a argument.
    def _centerWindow(self, window) -> None:
        # Get screen size
        screen = QApplication.primaryScreen()

        # Get geometry
        screen_geometry = screen.geometry()

        # Count half of creen
        x = (screen_geometry.width() - window.width()) // 2
        y = (screen_geometry.height() - window.height()) // 2

        # Move to center
        window.move(x, y)

    '''
    Mainwindow toolbar actions.
    '''

    # Open settings dialog
    def _openSettingsAction(self) -> None:
        # Create settings dialog object
        self.SettingsDialog = SettingsDialog(self.app)

        # Exec settings dialog
        self.SettingsDialog.exec()

    # Function that set target url and save it to variable.
    def _setTargetAction(self) -> None:
        # Create dialog
        self.targetDialog = QDialog(self)

        # Load Ui
        self.targetDialogUi = Ui_TargetDialog()

        # Setup Ui
        self.targetDialogUi.setupUi(self.targetDialog)

        # Adjust size of dialog
        self.targetDialog.adjustSize()

        # Show targetDialog
        self.targetDialog.show()

        # Connect _onCheckUrl to target button
        self.targetDialogUi.setTargetButton.clicked.connect(lambda: self._onCheckURL(self.targetDialogUi.setTargetLineEdit.text()))

    # Check if is target reachable, show message if not.
    def _checkURL(self, url) -> bool:
        # Try reach url
        try:
            # Get response using request module and head function, better variantion for all purposes with 5ms timeout
            r = requests.head(url, timeout=5, allow_redirects=True)

            # Check status code first if the server does not using head
            if r.status_code == 405:
                # Get new request with get and again 5ms timeout
                r = requests.get(url, timeout=5)

            # Return status code if is good
            return 200 <= r.status_code < 400
        except requests.RequestException as e:
            # Print error message 
            self.printe(exception=e, function=self._checkURL.__name__)

            return False

    # Function that is calling _checkURL with url parametr, is called from _setTargetAction.
    def _onCheckURL(self, url) -> None:
        # Check if URL is enetered or if is reachable
        if not self._checkURL(url): 
            # Set wrong url stylesheet for line edit (red border)
            self.targetDialogUi.setTargetLineEdit.setStyleSheet(
                "border: 2px solid red;"
            )
        else:
            # Close dialog if url is ok
            self.targetDialog.close()

            # Set url
            self.url = url

            # Change title
            self.setWindowTitle(f"{self.app.name} | {self.app.version} {f"| {self.url}" if self.url else ""}")  

            # Load page like requests and source code and other
            self._loadWebPage()

    # About action for open about dialog which is used to show inforamtion about this application like version and more.
    def _aboutAction(self) -> None:
        '''
        Load Ui for about dialog.
        '''
        # Create dialog
        aboutDialog = QDialog(self)

        # Load Ui
        aboutDialogUi = Ui_aboutDialog()

        # Set Ui
        aboutDialogUi.setupUi(aboutDialog)

        '''
        Dialog properties, size, title and other.
        '''

        # Set title 
        aboutDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | About")  

        # Adjust size for dialog
        aboutDialog.resize(aboutDialog.sizeHint())

        # Set version text to label 
        aboutDialogUi.versionLabel.setText(f"{aboutDialogUi.versionLabel.text()} {self.app.version}")

        # Show dialog
        aboutDialog.show()

    # Load page function that runs _getSource and other function for inspecting page.
    def _loadWebPage(self) -> None:
        # Get source code first and load it to text edit
        self.ui.sourceTextEdit.setPlainText(self._getSourceCode())

    # Download source from url which is get from set target menu and function.
    def _getSourceCode(self) -> str:
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

    '''
    Public functions.
    '''
    
    # Close event overwritten.
    def closeEvent(self, event) -> None:
        # Quit application
        QApplication.quit()