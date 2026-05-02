# SettingsDialog.py

from PySide6.QtWidgets import QDialog # type: ignore

from noctua.settings_dialog.source_page import SourcePage
from noctua.settings_dialog.general_page import GeneralPage
from noctua.settings_dialog.logging_page import LoggingPage
from noctua.ui_gen.SettingsDialog import Ui_SettingsDialog
from noctua.context import ctx

class SettingsDialog(QDialog):

    def __init__(self) -> None:

        super().__init__()

        # Load Ui and setup
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
    
        # General. logging and source page
        self.GeneralPage = GeneralPage
        self.SourcePage = SourcePage
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

        # Set first page and connect swithcin
        self._change_page(self.ui.settingsView.currentRow())
        self.ui.settingsView.currentRowChanged.connect(self._change_page)

        # Save, reset and cancel actions
        self.ui.applyButton.clicked.connect(self._save_settings)
        self.ui.resetButton.clicked.connect(self._reset_settings)
        self.ui.cancelButton.clicked.connect(self.close)

        # self.ui.applyButton.setEnabled(None)

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
        
    # Save settings from all pages
    def _save_settings(self) -> None:
        try:
            config = ctx.config

            for page in self.activePages:
                # Check if page exists
                if page:
                    if not page.isSaved:
                        pageName = type(page).__name__

                        # Get settings
                        config[pageName] = page.get_settings()

                        # Mark page as saved
                        page.isSaved = True

            # Save settings
            ctx.ConfigManager.save_settings(config)
            self.ui.statusLabel.setText(self.ui.statusLabel.text() + "SUCCESS")
        except Exception as e:
            # Show error
            self.ui.statusLabel.setText(self.ui.statusLabel.text() + "ERROR")

    # Reset configuration
    def _reset_settings(self) -> None:
        # Trigger the configuration handler to overwrite the current JSON with default values.
        ctx.ConfigManager.reset_settings()

        # Reload application config
        ctx.app.reload_config()

        # Browse active pages
        for page in self.activePages:
            if page and not isinstance(page, bool):
                page.load_settings(ctx.config.get(type(page).__name__, {}))

    # Overrided close event 
    @staticmethod
    def closeEvent(event) -> None:
        event.accept()