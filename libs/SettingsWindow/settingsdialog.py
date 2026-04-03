# settingswindow.py

# Module for managing settings window

# Importing system files
import sys
import os

from PySide6.QtWidgets import QDialog, QSlider, QComboBox, QWidget, QCheckBox # type: ignore
from PySide6.QtCore import QSignalBlocker # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Importing program files
from libs.Logging.logging import Logging
from resources.Themes.theme import Theme

from libs.QtGuiFiles.PyFiles.SettingsDialog import Ui_SettingsDialog
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog

# Class settings window
class SettingsDialog(QDialog, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents, save app and get all importants modules.
        '''

        # Init parents
        super().__init__()

        # Save application
        self.app = app

        # Save themes modules
        self.theme = self.app.theme

        # Save config module from app
        self.config = self.app.config

        # Print info message about settings window
        self.printi(msg="Opening settings window")

        '''
        All usefull variables.
        '''

        # Saved variable
        self.isSaved = True

        # Title for changing back from not saved status
        self.title = f"{self.app.name} | {self.app.version} | Settings"

        '''
        Load Ui file for settings dialog.
        '''

        # Load Ui file
        self.ui = Ui_SettingsDialog()

        # Setup Ui to QDialog
        self.ui.setupUi(self)

        '''
        Title, size, other dialog properties and actions.
        '''

        # Dialog properties like title, size and more
        self.setWindowTitle(self.title)

        # Set window icon
        self.setWindowIcon(QIcon(self.app.iconPath))

        # Set minimum size
        self.setMinimumSize(self.sizeHint())

        # Resize to default size
        self.resize(self.sizeHint())

        # Connect track changes for all childs
        self._changesTracking()

        # Pages changing actions
        self.ui.settingsView.currentRowChanged.connect(self.ui.settingsWidget.setCurrentIndex)

        # Save settings action
        self.ui.applyButton.clicked.connect(self._saveSettingsAction)

        # Save settings button enabled
        self.ui.applyButton.setEnabled(not self.isSaved)

        # Reset settings action
        self.ui.resetButton.clicked.connect(self._resetSettingsAction)

        # Cancel button action
        self.ui.cancelButton.clicked.connect(self.close)

        # Add all themes to theme combobox
        self.ui.themeComboBox.addItems(self.theme.themes())

        # Load settings
        self._loadSettings()

        '''
        General buttons actions.
        '''

        # Add theme button action
        self.ui.themeAddButton.clicked.connect(self.theme.themeDialog)

        # Resize
        self.resize(660, 528)

    '''
    Private functions.
    '''

    # Browse all keys and their values from config.json and set it for them.
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

    # Get value of all settings childs, make dictonary from it and overwrite config.json.
    def _saveSettingsAction(self) -> None:
        # Settings
        settings = {
            "askOnCloseComboBox": self.ui.askOnCloseComboBox.currentText(),
            "themeComboBox": self.ui.themeComboBox.currentText(),
            "stylesheetComboBox": self.ui.stylesheetComboBox.currentText(),
            "fontComboBox": self.ui.fontComboBox.currentText(),
            "fontSizeSlider": self.ui.fontSizeSlider.value(),
            "checkUpdatesComboBox": self.ui.checkUpdatesComboBox.currentText()
        }

        # Save settings in file
        self.config.saveSettings(settings)

        # Acutalize window
        self._loadSettings()

        # Change to saved
        self.isSaved = True

        # Set apply button to disabled if is all saved
        self.ui.applyButton.setEnabled(not self.isSaved)

        # Get back window title without *
        self.setWindowTitle(self.title)

        '''
        Load Ui for custom restart dialog because the changes will be applied after restart.
        '''

        # Create dialog for restart
        restartDialog = QDialog()

        # Load Ui for restart dialog
        restartDialogUi = Ui_customDialog()

        # Setup ui 
        restartDialogUi.setupUi(restartDialog)

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Set title for dialog
        restartDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Restart")

        # Adjust dialog size
        restartDialog.adjustSize()

        '''
        Set parametres for buttons and others childs.
        '''

        # Set label text
        restartDialogUi.textLabel.setText("Settings will be changed after restart. Do you want to restart?")

        # Set cancel button text
        restartDialogUi.cancelButton.setText("No")

        # Set sumbit button text
        restartDialogUi.sumbitButton.setText("Yes")

        # Set cancel button action
        restartDialogUi.cancelButton.clicked.connect(restartDialog.close)

        # Set sumbit button action
        restartDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Restarting application"), os.execv(sys.executable, [sys.executable] + sys.argv)))

        # Exec dialog, cant continue without response
        restartDialog.exec()

    # Reset settings function, open and rewrite config.json with self.config.default_config.
    def _resetSettingsAction(self) -> None:
        # Reset settings in file
        self.config.resetSettings()

        # Aktualize settings dialog
        self._loadSettings()

    # Connect function _markAsDirty for all child of some types.
    def _changesTracking(self):
        # Find all comboboxes
        for combo in self.findChildren(QComboBox):
            # Connect function
            combo.currentIndexChanged.connect(self._markAsDirty)
            
        # Find all sliders
        for slider in self.findChildren(QSlider):
            # Connect function
            slider.valueChanged.connect(self._markAsDirty)
            
        # Find all checkboxes
        for checkbox in self.findChildren(QCheckBox):
            # Connect function
            checkbox.stateChanged.connect(self._markAsDirty)
    
    # Function that change isSaved status if somethings is saved.
    def _markAsDirty(self) -> None:
        # Check if not saved
        if self.isSaved:
            # Change saved status
            self.isSaved = False

            # Change window title
            self.setWindowTitle(self.title + " *")

            # Enable button
            self.ui.applyButton.setEnabled(not self.isSaved)

    '''
    Public functions.
    '''

    # Qt close event overwritten.
    def closeEvent(self, event) -> None:
        # If it is saved
        if self.isSaved:
            # Show message for close
            self.printi(msg="Closing settings window")

            # And close through accept event method
            event.accept()

            return

        # If not saved, create dialog for user response if continue without saving or save
        closeDialog = QDialog(self) 
        
        # Load Ui
        closeDialogUi = Ui_customDialog()

        # Setup Ui
        closeDialogUi.setupUi(closeDialog)

        # Set dialog title
        closeDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Close settings")

        # Set information label text
        closeDialogUi.textLabel.setText("Settings not saved! Do you want to abort it?")

        # Set cancel button text 
        closeDialogUi.cancelButton.setText("Close without saving")

        # Set sumbit buttin text for saving
        closeDialogUi.sumbitButton.setText("Save & Close")
        
        # Set modalable 
        closeDialog.setModal(True)

        # Adjust dialog size
        closeDialog.adjustSize()

        # Cancel button connect to close dialog through cross button in title
        closeDialogUi.cancelButton.clicked.connect(closeDialog.reject)
        
        # Sumbit button connect for save and close
        closeDialogUi.sumbitButton.clicked.connect(closeDialog.accept)

        # Run dialog with resutl 
        result = closeDialog.exec()

        # Check result
        if result == QDialog.Accepted:
            # Show message save and quit
            self.printi(msg="Saving and quitting...")

            # Save settings
            self._saveSettingsAction() 

            # Accept event for close dialog
            event.accept() 
        elif result == QDialog.Rejected:
            # Close dialog and settings window msg that window is closing without saving settings
            self.printi(msg="Quitting without saving")

            # Accept event and close
            event.accept()
        else:
            # Ignore event if user just click close cross button
            event.ignore()