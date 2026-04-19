# SettingsDialog.py

# Module for managing settings window

# Importing system files
import re
import sys
import os

from PySide6.QtWidgets import QDialog # type: ignore
from PySide6.QtGui import QIcon # type: ignore

# Importing program files
from Application.SettingsDialog.SourcePage.SourcePage import SourcePage
from Application.SettingsDialog.GeneralPage.GeneralPage import GeneralPage
from Application.SettingsDialog.LoggingPage.LoggingPage import LoggingPage

from Application.QtFiles.SettingsDialog import Ui_SettingsDialog
from Application.QtFiles.CustomDialog import Ui_customDialog

# Class settings window
class SettingsDialog(QDialog):

    # Initiator
    def __init__(self, app) -> None:

        # Init parents
        super().__init__()

        # Config manager
        self.ConfigManager = app.ConfigManager

        # ThemeManager
        self.ThemesManager = app.ThemesManager

        # Config from config manager
        self.config = app.config

        # Load Ui file
        self.ui = Ui_SettingsDialog()

        # Setup Ui 
        self.ui.setupUi(self)
    
        # General page
        self.GeneralPage = GeneralPage

        # Source page
        self.SourcePage = SourcePage

        # Logging page
        self.LoggingPage = LoggingPage

        # All pages
        self.pages = [
            self.GeneralPage,
            self.LoggingPage,
            self.SourcePage
        ]

        # Actiave pages
        self.activePages = [
            False,
            False,
            False
        ]

        # Set general as a first page
        self._changePage(self.ui.settingsView.currentRow())

        # Pages changing actions
        self.ui.settingsView.currentRowChanged.connect(self._changePage)

        # Save settings action
        self.ui.applyButton.clicked.connect(self._saveSettingsAction)

        # Reset settings action
        self.ui.resetButton.clicked.connect(self._resetSettingsAction)

        # Cancel button action
        self.ui.cancelButton.clicked.connect(self.close)

    '''
    Private functions.
    '''

    # Load one page
    def _changePage(self, pageIndex) -> None:
        # If page isnt inicialized
        if not self.activePages[pageIndex]:
            # Inicialize page 
            newPage = self.pages[pageIndex](self)

            # Mark as inicialized
            self.activePages[pageIndex] = newPage

            # Insert it to stacked widget
            self.ui.settingsWidget.insertWidget(pageIndex, newPage)
        
            # Load settings
            newPage.loadSettings(self.config.get(type(newPage).__name__))

        # Show page
        self.ui.settingsWidget.setCurrentIndex(pageIndex)
        
    # Collects values from all UI widgets, saves them to a dictionary, and updates the configuration file.
    def _saveSettingsAction(self) -> None:
        # Create settings
        config = self.config

        # Browse all pages
        for page in self.activePages:
            # Check if page exists
            if page:
                # Check if saved
                if not page.isSaved:
                    # Get page name
                    pageName = type(page).__name__

                    # Get settings
                    config[pageName] = page.getSettings()

                    # Mark page as saved
                    page.isSaved = True

        # Write the settings dictionary to the physical configuration file via the config handler.
        self.ConfigManager.saveSettings(config)
    
        # Revert the window title to its original state, typically removing an unsaved '*' marker.
        # self.setWindowTitle(self.title)

    # Reverts the configuration file to its factory defaults and refreshes the settings interface.
    def _resetSettingsAction(self) -> None:
        # Trigger the configuration handler to overwrite the current JSON with default values.
        self.ConfigManager.resetSettings()

        # Reload application config
        self.app.reloadConfiguration()

        # Browse active pages
        for page in self.activePages:
            # Run only for real objects
            if page and not isinstance(page, bool):
                page.loadSettings(self.config.get(type(page).__name__, {}))

        # Loguru acitalization
        if hasattr(self, 'Logger'):
            self.app.Logger.updateConfig(self.config.get("LoggingPage", {}))
            
    '''
    Public functions.
    '''

    # Overriding the default Qt close event to handle unsaved changes.
    def closeEvent(self, event) -> None:
        '''
        Handles the window closure logic by checking if settings are saved.
        If changes are pending, it prompts the user with a confirmation dialog.
        '''
        
        # Browse pages
        for page in self.activePages:
            # Check if page exists
            if page:
                # Check the boolean flag that tracks if current settings are saved
                if page.isSaved:

                    # Tell Qt to proceed with closing the window
                    event.accept()

                    # Exit the function early as no further action is needed
                    return

        # Create a new modal dialog to warn the user about unsaved data
        closeDialog = QDialog(self) 
        
        # Instantiate the custom dialog UI layout
        closeDialogUi = Ui_customDialog()

        # Apply the UI components to the dialog instance
        closeDialogUi.setupUi(closeDialog)

        # Define the window title using application metadata
        closeDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Close settings")

        # Set the descriptive text informing the user about the unsaved state
        closeDialogUi.textLabel.setText("Settings not saved! Do you want to abort it?")

        # Configure the secondary button for discarding changes
        closeDialogUi.cancelButton.setText("Close without saving")

        # Configure the primary button for saving and then closing
        closeDialogUi.sumbitButton.setText("Save & Close")
        
        # Ensure the dialog blocks interaction with the parent window
        closeDialog.setModal(True)

        # Adjust the dialog dimensions to fit the newly set text and buttons
        closeDialog.adjustSize()

        # Link the discard button to the dialog's rejected result
        closeDialogUi.cancelButton.clicked.connect(closeDialog.reject)
        
        # Link the save button to the dialog's accepted result
        closeDialogUi.sumbitButton.clicked.connect(closeDialog.accept)

        # Execute the dialog modally and capture the user's choice
        result = closeDialog.exec()

        # Evaluate if the user chose the 'Save & Close' option
        if result == QDialog.Accepted:
            # Log the intent to save data before exiting
            # Execute the internal logic to write settings to storage
            self._saveSettingsAction() 

            # Allow the main window close event to proceed
            event.accept() 

        # Evaluate if the user chose to 'Close without saving'
        elif result == QDialog.Rejected:

            # Allow the main window close event to proceed despite lack of saving
            event.accept()

        # Handle cases where the user closes the dialog without a choice (e.g., Esc)
        else:
            # Cancel the window closure to keep the settings window open
            event.ignore()