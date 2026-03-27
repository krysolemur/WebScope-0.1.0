# application.py

# Import system files
import bcrypt
import json
import os
import sys

from PySide6.QtWidgets import QLabel, QApplication, QHBoxLayout, QPushButton, QComboBox, QLineEdit 
from PySide6.QtCore import QTimer
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon

# Importing program files
from libs.MainWindow.mainwindow import MainWindow
from libs.Logging.logging import Logging
from libs.Errors.errors import Error
from libs.Errors.exceptions import *

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self) -> None:
        '''
        Set application parametres, init parents and other.
        '''
        # Init parents
        super().__init__(sys.argv)

        # Info message
        self.printi(msg="Creating application")

        '''
        Setting all applications variables.
        '''

        # Application version
        self.version = "0.1.0"

        # Application name
        self.name = "WebScope"

        '''
        Inicializing all neccessary modules.
        '''

        # Error module
        self.error = Error()

        # Window module
        self.window = MainWindow(app=self)

        '''
        Running program.
        '''

        # Setup application
        self._setup()

    '''
    Private functions.
    '''

    # Setup function
    def _setup(self) -> None:
        '''
        Load ui for custom restart dialog.
        '''

        # Load Ui file
        ui_file = QFile("libs/QtGuiFiles/SetupDialog.ui")

        # Read Ui file
        ui_file.open(QFile.ReadOnly)

        # Load to setupDialog
        self.setupDialog = QUiLoader().load(ui_file)

        # Close Ui file
        ui_file.close()

        '''
        Set window properties, title, size and more.
        '''

        # Dialog properties like title, size and more
        self.setupDialog.setWindowTitle(f"{self.name} | {self.version} | Inicializing")

        # Window icon
        self.setupDialog.setWindowIcon(QIcon("icon.svg"))

        # Set size
        self.setupDialog.resize(600, 75)

        # Exec setupDialog
        self.setupDialog.show()

        '''
        Set timer for loading bar.
        '''
        
        # Process index
        self.process_index = 0

        # Run all setup processes 
        self._run_next_process()

    '''
    Setup dialog methods.
    '''

    # Run next proccess function
    def _run_next_process(self) -> None:
        # List of all proccesses with their labels
        all_process = [
            self._checkNetworkConnection,
            self._checkForUpdates,
            self._checkConfigDir
        ]

        '''
        Run all proccess with try except block for catching errors.
        '''

        # Check if all process were runned
        if self.process_index >= len(all_process):
            # Close setup dialog
            self.setupDialog.close()

            # Exec main window
            self.window.show()

            # End function
            return  

        # Try-except for catching errors
        try:    
            # Get proccess 
            process = all_process[self.process_index]

            # Set label text
            self.setupDialog.loadingLabel.setText(process.__name__)

            # Run process
            process()

            # Process events
            self.processEvents()

            '''
            Set label properties and loading bar actions.
            '''

            # Set OK Color
            self.setupDialog.statusLabel.setStyleSheet("color: #00ff00")

            # Set OK status of function
            self.setupDialog.statusLabel.setText("OK")

            # Set progressBar value
            self.setupDialog.loadingBar.setValue(self.setupDialog.loadingBar.value() + (100 // len(all_process)))

            # OK message
            self.printo(msg="", function=process.__name__)

            # Process events
            self.processEvents()
        except Exception as e:
            '''
            Set error look.
            '''

            # Error message
            self.printe(exception=e, msg="", function=self._run_next_process.__name__)

            # Set ERROR Color
            self.setupDialog.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.setupDialog.statusLabel.setText("ERROR")

        # Next index
        self.process_index += 1

        # Next function after 500ms
        QTimer.singleShot(500, self._run_next_process)

    # Checking internet connection
    def _checkNetworkConnection(self) -> None:
        None

    # Function that check for updates
    def _checkForUpdates(self) -> None:
        None

    # Checking config files
    def _checkConfigDir(self) -> None:
        None


    '''
    Public functions.
    '''
