# LoggingPage.py

# Importing system files
from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QWidget, QSpinBox, QLineEdit # type: ignore

# Importing program files
from Application.QtFiles.LoggingPage import Ui_LoggingPage

# Class with color picker
class LoggingPage(QWidget):
    
    # Initiator
    def __init__(self, parent) -> None:

        # Init parents
        super().__init__(parent)

        # Load page
        self.ui = Ui_LoggingPage()

        # Setup ui
        self.ui.setupUi(self)

        # Saved
        self.isSaved = True

        # Connect tracking changes for all widgets
        self._connectChangesTracking()

    '''
    Settings methods.
    '''

    # Load settings function
    def loadSettings(self, settings: dict) -> None:
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

    # Get settings from childs
    def getSettings(self) -> dict:
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
    
    '''
    Marking as not saved.
    '''

    # Automatically discovers input widgets and connects their change signals to the dirty state tracker.
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

    # Function that change isSaved status if somethings is saved.
    def _markAsDirty(self) -> None:
        # Change saved status
        self.isSaved = False
