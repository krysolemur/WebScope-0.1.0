# settingswindow.py

# Module for managing settings window

# Importing system files
import re
import os

from PySide6.QtWidgets import QDialog, QSlider, QComboBox, QWidget # type: ignore
from PySide6.QtCore import QSignalBlocker # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Importing program files
from libs.Logging.logging import Logging
from Config.configmanager import ConfigManager

from libs.QtGuiFiles.PyFiles.SettingsDialog import Ui_SettingsDialog
from libs.QtGuiFiles.PyFiles.ProfileDialog import Ui_ProfileDialog
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog
# Class settings window
class SettingsDialog(QDialog, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents, save app and print info message.
        '''
        # Init parents
        super().__init__()

        # Save application
        self.app = app

        # Print info message
        self.printi(msg="Opening settings window")

        '''
        All usefull variables.
        '''

        # Config module
        self.config = ConfigManager()

        # Saved variable
        self.saved = True

        '''
        Load Ui file for settings window menu.
        '''

        # Load Ui file
        self.ui = Ui_SettingsDialog()

        # Setup ui 
        self.ui.setupUi(self)

        '''
        Title, size, other settings and actions.
        '''

        # Dialog properties like title, size and more
        self.setWindowTitle(f"{self.app.name} | {self.app.version} | Settings")

        # Set window icon
        self.setWindowIcon(QIcon("icon.svg"))

        # Load settings
        self._loadSettings()

        # Pages actions
        self.ui.settingsView.currentRowChanged.connect(self.ui.settingsWidget.setCurrentIndex)

        # Save settings action
        self.ui.applyButton.clicked.connect(self._saveSettings)

        # Reset settings action
        self.ui.resetButton.clicked.connect(self._resetSettings)

        # Cancel button action
        self.ui.cancelButton.clicked.connect(self.close)

        # Resize
        self.resize(660, 528)

    '''
    Private functions.
    '''

    '''
    Settings methods
    '''

    # Save settings
    def _saveSettings(self) -> None:
        # Settings
        settings = {
            "askOnCloseComboBox": self.ui.askOnCloseComboBox.currentText(),
            "themeComboBox": self.ui.themeComboBox.currentText(),
            "fontComboBox": self.ui.fontComboBox.currentText(),
            "fontSizeSlider": self.ui.fontSizeSlider.value(),
            "checkUpdatesComboBox": self.ui.checkUpdatesComboBox.currentText()
        }

        # Save settings in file
        self.config.saveSettings(settings)

        # Acutalize window
        self._loadSettings()

    # Load settings
    def _loadSettings(self) -> None:
        # Get settings 
        settings = self.config._loadSettings()

        '''
        Set value for all objects.
        '''

        # Browse all keys and their value
        for key, value in settings.items():
            # Find child from name
            widget = self.findChild(QWidget, key) 
            
            # If there is child
            if widget:
                # Block signals
                blocker = QSignalBlocker(widget) 

                # Check instances
                if isinstance(widget, QComboBox):
                    # Load their value for combobox
                    widget.setCurrentText(str(value))
                elif isinstance(widget, QSlider):
                    # For slider
                    widget.setValue(int(value))
    
    # Reset settings
    def _resetSettings(self) -> None:
        # Reset settings in file
        self.config.resetSettings()

        # Aktualize settings dialog
        self._loadSettings()

    '''
    Public functions.
    '''

    # Close event
    def closeEvent(self, event) -> None:
        # Check if saved
        if not self.saved:
            # Create dialog
            closeDialog = QDialog()

            # Load ui
            closeDialogUi = Ui_customDialog()

            # Setup ui
            closeDialogUi.setupUi(closeDialog)

            '''
            Set properties for custom dialog, title, size and center it.
            '''

            # Set title
            closeDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Close settings")

            # Adjust dialog
            closeDialog.adjustSize()

            # Set dialog modal
            closeDialog.setModal(True)

            '''
            Set parametres for buttons and actions.
            '''

            # Set label text
            closeDialogUi.textLabel.setText("Settings not saved! Do you want to abort it?")

            # Set cancel button text
            closeDialogUi.cancelButton.setText("Close")

            # Set sumbit button text
            closeDialogUi.sumbitButton.setText("Save & close")

            # Set cancel action
            closeDialogUi.cancelButton.clicked.connect(self.close())

            # Set sumbit action
            closeDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Quiting application"), QApplication.quit()))

            # Show dialog
            closeDialog.exec()

            # Ignore event
            event.ignore()
        else:
            # Print message
            self.printi(msg="Closing settings window")

            # Close window
            event.accept()
