# settingswindow.py

# Module for managing settings window

# Importing system files
import re
import os

from PySide6.QtWidgets import QDialog, QVBoxLayout, QSizePolicy # type: ignore
from PySide6.QtCore import QFile # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Importing program files
from libs.Logging.logging import Logging
from Config.configmanager import ConfigManager

from libs.QtGuiFiles.PyFiles.SettingsDialog import Ui_SettingsDialog
from libs.QtGuiFiles.PyFiles.ProfileDialog import Ui_ProfileDialog

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

        # Add profiles into combobox
        self._loadProfiles()

        # Add profile action
        self.ui.addProfileButton.clicked.connect(self._addProfile)

        # Remove profile action
        self.ui.removeProfileButton.clicked.connect(self._removeProfile)

        # Pages actions
        self.ui.settingsView.currentRowChanged.connect(self.ui.settingsWidget.setCurrentIndex)

        # Remove button enabled only if config profile is not selected
        self.ui.profilesComboBox.currentTextChanged.connect((lambda text: self.ui.removeProfileButton.setEnabled(text != "config.json")))

        # Update it after window loads
        self.ui.removeProfileButton.setEnabled(self.ui.profilesComboBox.currentText() != "config.json")

        # Save settings action
        self.ui.applyButton.clicked.connect(lambda: self.config.saveSettings(self.ui.profilesComboBox.currentText()))

        # Reset settings action
        self.ui.resetButton.clicked.connect(lambda: self.config.resetSettings(self.ui.profilesComboBox.currentText()))

        # Cancel button action
        self.ui.cancelButton.clicked.connect(self.close)

        # Resize
        self.resize(660, 528)


    '''
    Private functions.
    '''

    '''
    Profiles methods.
    '''

    # Load profiles
    def _loadProfiles(self) -> None:
        # Clear combo box
        self.ui.profilesComboBox.clear()

        # Add all items to combobox
        self.ui.profilesComboBox.addItems(self.config.all_profiles())

    # Add profile
    def _addProfile(self) -> None:
        '''
        Load dialog.
        '''
        # Create dialog
        self.profileDialog = QDialog()

        # Load Ui file
        self.profileDialogUi = Ui_ProfileDialog()

        # Setup ui 
        self.profileDialogUi.setupUi(self.profileDialog)

        '''
        Dialog properties, title and cations.
        '''

        # Adjust size
        self.profileDialog.adjustSize()

        # Create button action
        self.profileDialogUi.createButton.clicked.connect(self._checkProfile)

        # Cancel button action
        self.profileDialogUi.cancelButton.clicked.connect(self.profileDialog.reject)

        # Show dialog
        self.profileDialog.exec()

    # Check profile function
    def _checkProfile(self) -> None:
        # Get name
        name = self.profileDialogUi.profileNameLineEdit.text().strip()

        # Set error styles
        self.profileDialogUi.statusLabel.setStyleSheet(
            "color: #ff0000"
        )

        # Check if profile is not None
        if not name or not bool(re.fullmatch(r'^[a-zA-Z0-9_\- ]+$', name)):
            # Set error label
            self.profileDialogUi.statusLabel.setText("Enter valid name!")

            return

        # Check if profile does not exists
        if os.path.exists(os.path.join(self.config.config_dir, f"{name}.json")):
            # Set error label
            self.profileDialogUi.statusLabel.setText(f"Profile with name {name} already exists!")
            
            return

        # Add profile
        self.config.addProfile(name)

        # Close dialog
        self.profileDialog.close()

        # Actualize profiles list
        self._loadProfiles()

    # Remove profile
    def _removeProfile(self) -> None:
        # Call config function
        self.config.removeProfile(self.ui.profilesComboBox.currentText())

        # Akutalize profiles
        self._loadProfiles()
        
    '''
    Public functions.
    '''

    # Close event
    def closeEvent(self, event) -> None:
        # Print message
        self.printi(msg="Closing settings window")

        # Close window
        event.accept()
