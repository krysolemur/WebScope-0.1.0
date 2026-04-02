# window.py

# Importing system files
import requests
import sys
import os

from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow, QMessageBox # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Imporing program files
from libs.Logging.logging import Logging
from libs.SettingsWindow.settingsdialog import SettingsDialog

from libs.QtGuiFiles.PyFiles.MainWindow import Ui_MainWindow
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog
from libs.QtGuiFiles.PyFiles.AboutDialog import Ui_aboutDialog

# Main class window for managing window and loading GUI
class MainWindow(QMainWindow, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents and save app object as a variable.
        '''
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

        '''
        Load UI for MainWindow.
        '''

        # Load Ui
        self.ui = Ui_MainWindow()

        # Set Ui
        self.ui.setupUi(self)

        '''
        Set actions for all menu in tool bar like settings, help and more...
        '''

        # Settings action
        self.ui.actionSettings.triggered.connect(self._openSettings)

        # Close action
        self.ui.actionQuit.triggered.connect(self.close)

        # Restart action
        self.ui.actionRestart.triggered.connect(self._restart)

        # About action
        self.ui.actionAbout.triggered.connect(self._about)

        # Set target action
        self.ui.actionSetTarget.triggered.connect(self._setTarget)

        '''
        Other windows settings like size, title and more...
        '''

        # Title
        self.setWindowTitle(f"{self.app.name} | {self.app.version}")  

        # Set window icon
        self.setWindowIcon(QIcon("icon.svg"))

        # Size
        self.resize(800, 600) 

        # Go to center of screen
        self._center(self)

    '''
    Private functions.
    '''

    # Center function
    def _center(self, window) -> None:
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

    # Settings function
    def _openSettings(self) -> None:
        # Create settings window object
        self.settingsDialog = SettingsDialog(app=self.app)

        # Exec settings window
        self.settingsDialog.exec()

    # Set target function
    def _setTarget(self) -> None:
        # Load QtUi file 
        ui_file = QFile("libs/QtGuiFiles/TargetDialog.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.targetDialog = QUiLoader().load(ui_file)

        # Close file
        ui_file.close()

        # Adjust size
        self.targetDialog.adjustSize()

        # Show target dialog
        self.targetDialog.show()

        # Set action button
        self.targetDialog.setTargetButton.clicked.connect(self._onCheckURL)

    # Check url function
    def _checkURL(self, url) -> bool:
        # Try reach url
        try:
            # Get response
            r = requests.head(url, timeout=5, allow_redirects=True)

            # Check status code first if the server does not using head
            if r.status_code == 405:
                # Get new request
                r = requests.get(url, timeout=5)

            # Return status code
            return 200 <= r.status_code < 400
        except requests.RequestException as e:
            # Print error
            self.printe(exception=e, function=self._checkURL.__name__, )

            # Return false
            return False

    # Button action
    def _onCheckURL(self) -> None:
        # Get URL
        url = self.targetDialog.setTargetLineEdit.text()

        # Check URL
        if not self._checkURL(url): 
            # Set wrong URL stylesheet
            self.targetDialog.setTargetLineEdit.setStyleSheet(
                "border: 2px solid red;"
            )
        else:
            # Close dialog
            self.targetDialog.close()

    # Restart function
    def _restart(self, event) -> None:
        '''
        Load ui for custom restart dialog.
        '''

        # Load Ui
        self.restartDialog = QDialog()

        self.restartDialogUi = Ui_customDialog()

        # Setup ui 
        self.restartDialogUi.setupUi(self.restartDialog)

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title
        self.restartDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Restart")

        # Adjust dialog
        self.restartDialog.adjustSize()

        '''
        Set parametres for buttons and others childs.
        '''

        # Set label text
        self.restartDialogUi.textLabel.setText("Do you really want to restart application?")

        # Set cancel button text
        self.restartDialogUi.cancelButton.setText("No")

        # Set sumbit button text
        self.restartDialogUi.sumbitButton.setText("Yes")

        # Set cancel button action
        self.restartDialogUi.cancelButton.clicked.connect(self.restartDialog.close)

        # Set sumbit button action
        self.restartDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Restarting application"), os.execv(sys.executable, [sys.executable] + sys.argv)))

        # Show dialog
        self.restartDialog.exec()

    # About action
    def _about(self) -> None:
        '''
        Load ui for about dialog.
        '''
        # Create dialog
        self.aboutDialog = QDialog()

        # Load Ui
        self.aboutUi = Ui_aboutDialog()

        # Set Ui
        self.aboutUi.setupUi(self.aboutDialog)

        '''
        Dialog properties, size, title and other.
        '''

        # Set title
        self.aboutDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | About")  

        # Adjust size
        self.aboutDialog.resize(self.aboutDialog.sizeHint())

        # Set version text
        self.aboutUi.versionLabel.setText(f"{self.aboutUi.versionLabel.text()} {self.app.version}")

        # Show dialog
        self.aboutDialog.show()

    '''
    Public functions.
    '''
    
    # Close event
    def closeEvent(self, event) -> None:
        '''
        Load ui for custom close dialog.
        '''

        # Load Ui
        closeDialog = QDialog()

        closeDialogUi = Ui_customDialog()

        # Setup ui 
        closeDialogUi.setupUi(closeDialog)
        '''
        Set properties for custom dialog, title, size and center it.
        '''

        # Set title
        closeDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Close")

        # Adjust dialog
        closeDialog.adjustSize()

        # Set dialog modal
        closeDialog.setModal(True)

        '''
        Set parametres for buttons and actions.
        '''

        # Set label text
        closeDialogUi.textLabel.setText("Do you really want to quit application?")

        # Set cancel button text
        closeDialogUi.cancelButton.setText("No")

        # Set sumbit button text
        closeDialogUi.sumbitButton.setText("Yes")

        # Set cancel action
        closeDialogUi.cancelButton.clicked.connect(closeDialog.close)

        # Set sumbit action
        closeDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Quiting application"), QApplication.quit()))

        # Show dialog
        closeDialog.exec()

        # Ignore event
        event.ignore()