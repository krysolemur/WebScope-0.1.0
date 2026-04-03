# window.py

# Importing system files
import requests
import sys
import os

from PySide6.QtWidgets import QDialog, QApplication, QMainWindow # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Imporing program files
from libs.Logging.logging import Logging
from libs.SettingsWindow.settingsdialog import SettingsDialog

from libs.QtGuiFiles.PyFiles.MainWindow import Ui_MainWindow
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog
from libs.QtGuiFiles.PyFiles.AboutDialog import Ui_aboutDialog
from libs.QtGuiFiles.PyFiles.TargetDialog import Ui_TargetDialog

# Main class window for managing window and loading GUI
class MainWindow(QMainWindow, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents and save app object as a variable, load all important modules from it.
        '''
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

        # Config 
        self.config = self.app.config

        '''
        Load UI for MainWindow.
        '''

        # Load Ui
        self.ui = Ui_MainWindow()

        # Setup Ui for self (QMainWindow)
        self.ui.setupUi(self)

        '''
        Set actions for all menu in tool bar like settings, help and more...
        '''

        # Settings menu action
        self.ui.actionSettings.triggered.connect(self._openSettingsAction)

        # Close menu action
        self.ui.actionQuit.triggered.connect(self.close)

        # Restart menu action
        self.ui.actionRestart.triggered.connect(self.app.restartApplication)

        # About menu action
        self.ui.actionAbout.triggered.connect(self._aboutAction)

        # Set target menu action
        self.ui.actionSetTarget.triggered.connect(self._setTargetAction)

        '''
        Other windows properties like size, title and more...
        '''

        # Window title
        self.setWindowTitle(f"{self.app.name} | {self.app.version}")  

        # Window icon
        self.setWindowIcon(QIcon(self.app.iconPath))

        # Default size
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

    # Settings function for opening settings dialog from settingsdialog.py.
    def _openSettingsAction(self) -> None:
        # Create settings window object
        self.settingsDialog = SettingsDialog(self.app)

        # Exec settings window
        self.settingsDialog.exec()

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

    '''
    Public functions.
    '''
    
    # Close event overwritten.
    def closeEvent(self, event) -> None:
        # Quit application wihtout asking if it is set like that.
        if self.config.configuration["askOnCloseComboBox"] == "No":
            # Quit without asking
            QApplication.quit()

        '''
        Load Ui for custom close dialog.
        '''

        # Load Ui
        closeDialog = QDialog(self)

        # Load ui
        closeDialogUi = Ui_customDialog()

        # Setup ui 
        closeDialogUi.setupUi(closeDialog)

        '''
        Set properties for custom dialog, title, size and center it.
        '''

        # Set dialog title
        closeDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Close")

        # Adjust dialog size
        closeDialog.adjustSize()

        # Set dialog modalable
        closeDialog.setModal(True)

        '''
        Set parametres for buttons and actions.
        '''

        # Set info label text
        closeDialogUi.textLabel.setText("Do you really want to quit application?")

        # Set cancel button text
        closeDialogUi.cancelButton.setText("No")

        # Set sumbit button text
        closeDialogUi.sumbitButton.setText("Yes")

        # Set cancel action -> close dialog
        closeDialogUi.cancelButton.clicked.connect(closeDialog.close)

        # Set sumbit action -> close whole application
        closeDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Quiting application"), QApplication.quit()))

        # Show dialog
        closeDialog.exec()

        # After dialog closed, ignore event
        event.ignore()