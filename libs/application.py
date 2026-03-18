# application.py

# Importing
import requests
import sys
import os
import math

from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Importing program files
from libs.Window.window import Window
from libs.ConfigManager.configmanager import Config
from libs.Logging.logging import Logging
from libs.Errors.errors import Error

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self):
        # Init parents
        super().__init__(sys.argv)

        # Start QTimer
        self.timer = QTimer()

        # Info message
        self.printf(msg="Creating application", status="INFO")

        '''
        Setting all applications variables.
        '''

        # List of all proccesses with their labels
        self.all_proccess = [
            (self.checkForUpdates, "Checking for updates..."),
            (self.checkConfigDir, "Checkfing config directory...")
        ]

        # Application version
        self.version = "0.1.0"

        '''
        Inicializing all neccessary modules.
        '''

        # Window module
        self.window = Window(app=self)

        # Config module
        self.config = Config(parent=self)

        # Error module
        self.error = Error(parent=self)

        '''
        Running program.
        '''

        # Setup application
        self._setup()

    # Setup function
    def _setup(self) -> None:
        # Print DEBUG
        self.printf(status="DEBUG", msg="Inicializing application")
        # Process index variable
        self.process_index = 0

        # Load Ui file
        ui_file = QtCore.QFile("QtGuiFiles/SetupWindow.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to setupWindow
        self.setupWindow = QtUiTools.QUiLoader().load(ui_file)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        # Dialog properties like title, size and more
        self.setupWindow.setWindowTitle(f"WebScope | {self.version}")

        # Set size
        self.setupWindow.setFixedSize(600, 75)

        # Set window icon
        self.setupWindow.setWindowIcon(QtGui.QIcon("Application/assets/icons/icon.png"))

        # Exec setupWindow
        self.setupWindow.show()

        # Run all setup processes with pause
        self.timer.timeout.connect(self._run_next_process)

        # Small pause
        self.timer.start(500)

    # Run next proccess function
    # No logging
    def _run_next_process(self):
        # Check if all process was runned
        if self.process_index == len(self.all_proccess):
            # Stop timer
            self.timer.stop()

            # Close loading window
            self.setupWindow.close()

            # Show main window
            self.window.show()

            # End loop 
            return

        # Get one process
        process = self.all_proccess[self.process_index]

        # Try-except for catching errors
        try:    
            # Check if process is call able
            if callable(process[0]):
                # Run process
                process[0]()

            # Set loading label text
            self.setupWindow.loadingLabel.setText(process[1])

            # Set OK Color
            self.setupWindow.statusLabel.setStyleSheet("color: #00ff00")

            # Set OK status of function
            self.setupWindow.statusLabel.setText("OK")

            # Set progressBar value
            self.setupWindow.loadingBar.setValue(self.setupWindow.loadingBar.value() + (100 // len(self.all_proccess)))

            # OK message
            self.printf(status="OK", msg="", function=process[0].__name__)
        except Exception as e:
            # Error message
            self.printf(status="ERROR", exception=e, msg="")

            # Set ERROR Color
            self.setupWindow.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.setupWindow.statusLabel.setText("ERROR")

            # Stop timer
            self.timer.stop()

        # Count + 1 process index
        self.process_index += 1

    # Function that check for updates
    def checkForUpdates(self):
        None

    # Checking config files
    def checkConfigDir(self):
        None