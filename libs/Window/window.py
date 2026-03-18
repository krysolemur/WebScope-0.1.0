# window.py

# Importing Qt
from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Main class window for managing window and loading GUI
class Window(QMainWindow):
    def __init__(self, app) -> None:
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

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

        # Title
        self.setWindowTitle(f"WebScope | {self.app.version}")  

        # Size
        self.resize(800, 600) 

        # Go to center of screen
        self._center()

    # Center function
    # No logging
    def _center(self) -> None:
        # Get screen size
        screen = QApplication.primaryScreen()

        # Get geometry
        screen_geometry = screen.geometry()

        # Count half of creen
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Move to center
        self.move(x, y)