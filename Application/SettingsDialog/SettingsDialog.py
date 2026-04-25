# SettingsDialog.py

from PySide6.QtWidgets import QDialog # type: ignore

from Application.SettingsDialog.SourcePage.SourcePage import SourcePage
from Application.SettingsDialog.GeneralPage.GeneralPage import GeneralPage
from Application.SettingsDialog.LoggingPage.LoggingPage import LoggingPage

from Application.QtFiles.SettingsDialog import Ui_SettingsDialog

from Application.AppContext import ctx

from Application.Logger.Logger import logger

class SettingsDialog(QDialog):

    def __init__(self) -> None:

        logger.info("Opening settings.")

        super().__init__()

        # Config manager
        self.ConfigManager = ctx.ConfigManager

        # Config from config manager
        self.config = ctx.config

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
        self._change_page(self.ui.settingsView.currentRow())

        # Pages changing actions
        self.ui.settingsView.currentRowChanged.connect(self._change_page)

        # Save settings action
        self.ui.applyButton.clicked.connect(self._save_settings)

        # Reset settings action
        self.ui.resetButton.clicked.connect(self._reset_settings)

        # Cancel button action
        self.ui.cancelButton.clicked.connect(self.close)

    # Load one page
    def _change_page(self, pageIndex) -> None:
        # If page isnt inicialized
        if not self.activePages[pageIndex]:
            # Inicialize page 
            newPage = self.pages[pageIndex](self)

            # Mark as inicialized
            self.activePages[pageIndex] = newPage

            # Insert it to stacked widget
            self.ui.settingsWidget.insertWidget(pageIndex, newPage)

        # Show page
        self.ui.settingsWidget.setCurrentIndex(pageIndex)
        
    # Collects values from all UI widgets, saves them to a dictionary, and updates the configuration file.
    def _save_settings(self) -> None:
        try:
            config = self.config

            for page in self.activePages:
                # Check if page exists
                if page:
                    if not page.isSaved:
                        pageName = type(page).__name__

                        # Get settings
                        config[pageName] = page.getSettings()

                        # Mark page as saved
                        page.isSaved = True

            # Save settings
            self.ConfigManager.saveSettings(config)
            self.ui.statusLabel.setText(self.ui.statusLabel.text() + "SUCCESS")
            logger.success("Settings saved.")
        except Exception as e:
            self.ui.statusLabel.setText(self.ui.statusLabel.text() + "ERROR")
            logger.error("Error while saving settings!")

    # Reset configuration
    def _reset_settings(self) -> None:
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

    # Overrided close event 
    def closeEvent(self, event) -> None:
        # Browse pages
        # for page in self.activePages:
        #     # Check if page exists
        #     if page:
        #         # Check the boolean flag that tracks if current settings are saved
        #         if page.isSaved:

        #             # Tell Qt to proceed with closing the window
        #             event.accept()

        #             # Exit the function early as no further action is needed
        #             return

        # Log and close
        logger.info("Closing settings.")
        event.accept()