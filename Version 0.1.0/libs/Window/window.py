# window.py

# Importing system files
import sys
import os

from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow, QMessageBox # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Imporing program files
from libs.Logging.logging import Logging
from libs.SettingsWindow.settingswindow import SettingsWindow

# Main class window for managing window and loading GUI
class Window(QMainWindow, Logging):
    def __init__(self, app) -> None:
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

        '''
        Load user interface 
        '''

        # Load QtUi file 
        ui_file = QFile("QtGuiFiles/MainWindow.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.ui = QUiLoader().load(ui_file)

        # Set central widget
        self.setCentralWidget(self.ui)

        # Close file
        ui_file.close()

        # Process events
        QtWidgets.QApplication.processEvents()

        '''
        Set actions for all menu in tool bar like settings, help and more...
        '''

        self.ui.actionSettings.triggered.connect(self._openSettings)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionRestart.triggered.connect(self._restart)

        '''
        Other windows settings like size, title and more...
        '''

        # Title
        self.setWindowTitle(f"WebScope | {self.app.version}")  

        # Size
        self.resize(800, 600) 

        # Go to center of screen
        self._center(self)

    '''
    Private functions.
    '''

    # Center function
    # No logging
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
    def _openSettings(self):
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
        ui_file = QFile("QtGuiFiles/CustomDialog.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.restartDialog = QUiLoader().load(ui_file, parent=self)

        # Close file
        ui_file.close()

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title
        self.restartDialog.setWindowTitle(f"WebScope | {self.app.version} | Restart")

        # Adjust dialog
        self.restartDialog.adjustSize()
        
        # Center dialog
        self._center(self.restartDialog)

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
        self.restartDialog.sumbitButton.clicked.connect(lambda: (self.printf(status="INFO", msg="Restarting application"), os.execv(sys.executable, [sys.executable] + sys.argv)))

        # Show dialog
        self.restartDialog.exec()

    '''
    Public functions.
    '''
    
    # Close event
    def closeEvent(self, event) -> None:
        '''
        Load ui for custom close dialog.
        '''

        # Load QtUi file for close dialog
        ui_file = QFile("QtGuiFiles/CustomDialog.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.closeDialog = QUiLoader().load(ui_file)

        # Close file
        ui_file.close()

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title
        self.closeDialog.setWindowTitle(f"WebScope | {self.app.version} | Close")

        # Adjust dialog
        self.closeDialog.adjustSize()
        
        # Center dialog
        self._center(self.closeDialog)

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
        self.closeDialog.sumbitButton.clicked.connect(lambda: (self.printf(status="INFO", msg="Quiting application"), QApplication.quit()))

        # Show dialog
        self.closeDialog.exec()

        # Ignore event
        event.ignore()