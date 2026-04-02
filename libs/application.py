# application.py

# Import system files
import json
import os
import sys

from PySide6.QtWidgets import QApplication, QDialog # type: ignore
from PySide6.QtCore import QTimer # type: ignore

# Importing program files
from libs.MainWindow.mainwindow import MainWindow
from Config.configmanager import ConfigManager
from libs.Logging.logging import Logging
from libs.Errors.errors import Error
from libs.Errors.exceptions import *

from libs.QtGuiFiles.PyFiles.SetupDialog import Ui_setupDialog

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self) -> None:
        '''
        Set application parametres, init parents and other.
        '''
        # Init parents
        super().__init__(sys.argv)

        # Init config module
        self.config = ConfigManager()

        '''
        Setting all applications variables.
        '''

        # Application version
        self.version = "0.1.0"

        # Application name
        self.name = "XyraEngine"

        '''
        Load ui for custom restart dialog.
        '''
        
        # Create dialog
        self.setupDialog = QDialog()

        # Load Ui file
        self.ui = Ui_setupDialog()

        # Setup ui 
        self.ui.setupUi(self.setupDialog)

        '''
        Set window properties, title, size and more.
        '''

        # Dialog properties like title, size and more
        self.setupDialog.setWindowTitle(f"{self.name} | {self.version} | Inicializing")

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

        # Window module
        self.window = MainWindow(app=self)

    '''
    Private functions.
    '''

    # Run next proccess function
    def _run_next_process(self) -> None:
        # List of all proccesses with their labels
        all_process = [
            self._checkNetworkConnection,
            self._checkForUpdates,
            self._checkConfigDir,
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

            # Run process
            process()

            # Process events
            self.processEvents()

            '''
            Set label properties and loading bar actions.
            '''

            # Set OK Color
            self.ui.statusLabel.setStyleSheet("color: #00ff00")

            # Set OK status of function
            self.ui.statusLabel.setText("OK")

            # Set progressBar value
            self.ui.loadingBar.setValue(self.ui.loadingBar.value() + (100 // len(all_process)))

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
            self.ui.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.ui.statusLabel.setText("ERROR")

        # Next index
        self.process_index += 1

        # Next function after 500ms
        QTimer.singleShot(500, self._run_next_process)

    # Checking internet connection
    def _checkNetworkConnection(self) -> None:
        # Set label text
        self.ui.loadingLabel.setText("Checking for internet connection")

    # Function that check for updates
    def _checkForUpdates(self) -> None:
        # Set label text
        self.ui.loadingLabel.setText("Checking for updates")

    # Checking config files
    def _checkConfigDir(self) -> None:
        # Set label text
        self.ui.loadingLabel.setText("Checking config directory")

    '''
    Public functions.
    '''
