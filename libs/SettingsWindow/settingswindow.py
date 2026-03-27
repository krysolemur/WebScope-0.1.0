# settingswindow.py

# Module for managing settings window

# Importing system files
from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import QFile 
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon 

# Importing program files
from libs.Logging.logging import Logging

# Class settings window
class SettingsWindow(QDialog, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents, save app and print info message.
        '''
        # Init parents
        super().__init__()

        # Save application
        self.app = app

        # Print info message
        self.printi(msg="Opening settings menu")

        '''
        Load user interface file to settings window menu.
        '''

        # Load Ui file
        ui_file = QFile("libs/QtGuiFiles/SettingsDialog.ui")

        # Read Ui file
        ui_file.open(QFile.ReadOnly)

        # Load to settingsWindow
        self.ui = QUiLoader().load(ui_file)

        # Create layout
        self.layout = QVBoxLayout()

        # Add ui to the layout
        self.layout.addWidget(self.ui)

        # Delete edges from layout
        self.layout.setContentsMargins(0, 0, 0, 0) 

        # Set layout to settings dialog
        self.setLayout(self.layout)

        # Close Ui file
        ui_file.close()

        # Process events
        self.app.processEvents()

        '''
        Title, size and other settings.
        '''

        # Dialog properties like title, size and more
        self.setWindowTitle(f"{self.app.name} | {self.app.version} | Settings")

        # Set window icon
        self.setWindowIcon(QIcon("icon.svg"))

        # Set size
        self.setFixedSize(622, 514)

    '''
    Public functions.
    '''

    # Close event
    def closeEvent(self, event) -> None:
        # Print message
        self.printi(msg="Closing settings window")

        # Close window
        event.accept()
