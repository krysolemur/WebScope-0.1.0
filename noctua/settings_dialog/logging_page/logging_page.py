# LoggingPage.py

from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QWidget, QSpinBox, QLineEdit, QFileDialog # type: ignore

from noctua.ui_gen.LoggingPage import Ui_LoggingPage
from noctua.context import ctx

class LoggingPage(QWidget):
    
    def __init__(self, parent) -> None:

        super().__init__(parent)

        # Load page
        self.ui = Ui_LoggingPage()

        # Setup ui
        self.ui.setupUi(self)

        # Load settings
        self.load_settings(ctx.config.get("LoggingPage"))

        # Saved
        self.isSaved = True

        # Connect tracking changes for all widgets
        self._connectChangesTracking()

        # Browse button action
        self.ui.btn_file_browse.clicked.connect(self._browse_log_folder)

        # Set file levels enabled or disabled
        self._file_levels(self.ui.cb_file_enabled.currentText())

        # Connect cb_file_enabled on changed text
        self.ui.cb_file_enabled.currentTextChanged.connect(self._file_levels)

    # Enable/disable file levels
    def _file_levels(self, text) -> None:
        # If yes, set enabled else disabled
        enable = text == "Yes"
        self.ui.btn_file_debug.setEnabled(enable)
        self.ui.btn_file_error.setEnabled(enable)
        self.ui.btn_file_info.setEnabled(enable)
        self.ui.btn_file_warning.setEnabled(enable)
        self.ui.btn_file_success.setEnabled(enable)

    # Browse log folder
    def _browse_log_folder(self) -> None:
        # Open dialog
        selected_directory = QFileDialog.getExistingDirectory(
            self, 
            "Select Folder for Logs",
            self.ui.le_file_path.text() or "." 
        )

        # If was selected
        if selected_directory:
            # Set path to line edit
            self.ui.le_file_path.setText(selected_directory)

    # Load settings 
    def load_settings(self, settings: dict) -> None:
        # Save settings reference
        self.settings = settings

        # Browse all keys and their values
        for key, value in settings.items():
            # Get widget by name from the UI object
            widget = getattr(self.ui, key, None)

            # If widget is None, skip (protects against old config keys)
            if widget is None:
                continue
            
            # Block signals to prevent triggering "onChanged" events during loading
            widget.blockSignals(True)

            # QPushButton 
            if isinstance(widget, QPushButton):
                if widget.isCheckable():
                    widget.setChecked(bool(value))

            # QCheckBox 
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))

            # QComboBox 
            elif isinstance(widget, QComboBox):
                index = widget.findText(str(value))
                if index >= 0:
                    widget.setCurrentIndex(index)

            # QSpinBox 
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except (ValueError, TypeError):
                    pass 

            # QLineEdit
            elif isinstance(widget, QLineEdit):
                widget.setText(str(value))

            # Unblock signals
            widget.blockSignals(False)

    # Get settings 
    def get_settings(self) -> dict:
        # Return settings
        return {
            # Console settings 
            "cb_console_time": self.ui.cb_console_time.currentText(),
            "cb_console_colors": self.ui.cb_console_colors.currentText(),
            "btn_console_info": self.ui.btn_console_info.isChecked(),
            "btn_console_warning": self.ui.btn_console_warning.isChecked(),
            "btn_console_success": self.ui.btn_console_success.isChecked(),
            "btn_console_error": self.ui.btn_console_error.isChecked(),
            "btn_console_debug": self.ui.btn_console_debug.isChecked(),

            # File logging settings
            "cb_file_enabled": self.ui.cb_file_enabled.currentText(),
            "btn_file_info": self.ui.btn_file_info.isChecked(),
            "btn_file_warning": self.ui.btn_file_warning.isChecked(),
            "btn_file_success": self.ui.btn_file_success.isChecked(),
            "btn_file_error": self.ui.btn_file_error.isChecked(),
            "btn_file_debug": self.ui.btn_file_debug.isChecked(),
            
            # Path, rotation
            "sb_file_rotation": self.ui.sb_file_rotation.value(),      
            "sb_file_retention": self.ui.sb_file_retention.value(),  
            "le_file_path": self.ui.le_file_path.text(),        
            "cb_file_compression": self.ui.cb_file_compression.currentText() 
        }
    
    # Connect marking for all widgets
    def _connectChangesTracking(self) -> None:
        container = self.ui.sa_content
        # Locate all combo box widgets within the current window and its children.
        for combo in container.findChildren(QComboBox):
            # Trigger the dirty flag whenever a different item is selected in a combo box.
            combo.currentIndexChanged.connect(self._markAsDirty)
            
        # Locate all slider widgets within the UI.
        for slider in container.findChildren(QSlider):
            # Trigger the dirty flag whenever the slider handle is moved to a new value.
            slider.valueChanged.connect(self._markAsDirty)
            
        # Locate all checkbox widgets within the UI.
        for checkbox in container.findChildren(QCheckBox):
            # Trigger the dirty flag whenever a checkbox is toggled on or off.
            checkbox.stateChanged.connect(self._markAsDirty)

        # Locate all push button widgets within the UI.
        for button in container.findChildren(QPushButton):
            # Check if is checkabel
            if button.isCheckable():
                # Connect the toggle signal to the dirty state tracker for checkable buttons.
                button.clicked.connect(self._markAsDirty)

    # Mark page as not saved
    def _markAsDirty(self) -> None:
        # Change saved status
        self.isSaved = False
