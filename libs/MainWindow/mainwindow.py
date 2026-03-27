# window.py

# Importing system files
import requests
import sys
import os

from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui 
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow, QMessageBox 
from PySide6.QtCore import QTimer, QFile 
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtGui import QIcon 

# Imporing program files
from libs.Logging.logging import Logging
from libs.SettingsWindow.settingswindow import SettingsWindow

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
        Load user interface 
        '''

        # Load QtUi file 
        ui_file = QFile("libs/QtGuiFiles/MainWindow.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.ui = QUiLoader().load(ui_file)

        # Set central widget
        self.setCentralWidget(self.ui)

        # Close file
        ui_file.close()

        '''
        Set actions for all menu in tool bar like settings, help and more...
        '''

        # Settings action
        self.ui.actionSettings.triggered.connect(self._openSettings)

        # Close action
        self.ui.actionQuit.triggered.connect(self.close)

        # Restart action
        self.ui.actionRestart.triggered.connect(self._restart)

        # Set target action
        self.ui.actionSetTarget.triggered.connect(self._setTarget)

        '''
        Other windows settings like size, title and more...
        '''

        # Title
        self.setWindowTitle(f"{self.app.name} | {self.app.version}")  

        # Set window icon
        self.setWindowIcon(QIcon("icon.png"))

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

    # Settings function
    def _openSettings(self) -> None:
        # Create settings window object
        self.settingsWindow = SettingsWindow(app=self.app)

        # Exec settings window
        self.settingsWindow.exec()

    # Restart function
    def _restart(self, event) -> None:
        '''
        Load ui for custom restart dialog.
        '''

        # Load QtUi file for close dialog
        ui_file = QFile("libs/QtGuiFiles/CustomDialog.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.restartDialog = QUiLoader().load(ui_file, self)

        # Close file
        ui_file.close()

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title
        self.restartDialog.setWindowTitle(f"WebScope | {self.app.version} | Restart")

        # Adjust dialog
        self.restartDialog.adjustSize()

        '''
        Set parametres for buttons and others childs.
        '''

        # Set label text
        self.restartDialog.textLabel.setText("Do you really want to restart application?")

        # Set button texts
        self.restartDialog.cancelButton.setText("No")
        self.restartDialog.sumbitButton.setText("Yes")

        # Set actions 
        self.restartDialog.cancelButton.clicked.connect(self.restartDialog.close)
        self.restartDialog.sumbitButton.clicked.connect(lambda: (self.printi(msg="Restarting application"), os.execv(sys.executable, [sys.executable] + sys.argv)))

        # Show dialog
        self.restartDialog.exec()
        
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

    # Check url function
    def _checkURL(self, url) -> bool:
        # Try reach url
        try:
            # Get response
            r = requests.get(url)
        except requests.RequestException as e:
            self.printe(exception=e, function=self._checkURL.__name, )

    '''
    Public functions.
    '''
    
    # Close event
    def closeEvent(self, event) -> None:
        '''
        Load ui for custom close dialog.
        '''

        # Load QtUi file for close dialog
        ui_file = QFile("libs/QtGuiFiles/CustomDialog.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.closeDialog = QUiLoader().load(ui_file, self)

        # Close file
        ui_file.close()

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title
        self.closeDialog.setWindowTitle(f"WebScope | {self.app.version} | Close")

        # Adjust dialog
        self.closeDialog.adjustSize()

        # Set dialog modal
        self.closeDialog.setModal(True)

        '''
        Set parametres for buttons and others childs.
        '''

        # Set label text
        self.closeDialog.textLabel.setText("Do you really want to quit application?")

        # Set button texts
        self.closeDialog.cancelButton.setText("No")
        self.closeDialog.sumbitButton.setText("Yes")

        # Set actions 
        self.closeDialog.cancelButton.clicked.connect(self.closeDialog.close)
        self.closeDialog.sumbitButton.clicked.connect(lambda: (self.printi(msg="Quiting application"), QApplication.quit()))

        # Show dialog
        self.closeDialog.exec()

        # Ignore event
        event.ignore()