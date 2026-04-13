# generalpage.py

# Import system files
from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QWidget # type: ignore

# Import program files
from Application.QtFiles.GeneralPage import Ui_generalPage

# Main class GeneralPage
class GeneralPage(QWidget):

    # Initiator
    def __init__(self, parent) -> None:

        # Init parents
        super().__init__(parent)

        # Config variable
        self.config = parent.config

        # Load page Ui
        self.ui = Ui_generalPage()

        # Setup Ui to QDialog
        self.ui.setupUi(self)

        # Saved variable
        self.isSaved = True

        # Connect tracking changes for all widgets
        self._connectChangesTracking()
                
        # Add all themes to theme combobox
        # self.ui.themeComboBox.addItems(self.theme.themes())

        # Add theme button action
        # self.ui.themeAddButton.clicked.connect(self.theme.getTheme)

    '''
    Settings methods.
    '''

    # Load settings function
    def loadSettings(self, settings) -> None:
        # Save settings
        self.settings = settings
        
        # Browse all keys and their values
        for key, value in settings.items():
            # Get widget by name
            widget = getattr(self.ui, key, None)

            # If widget is None, skip
            if widget is None:
                continue

            widget.blockSignals(True)

            # Check instances
            if isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QComboBox):
                index = widget.findText(str(value))
                if index >= 0:
                    widget.setCurrentIndex(index)
            elif isinstance(widget, QSlider):
                widget.setValue(int(value))
            elif isinstance(widget, QPushButton):
                if widget.isCheckable():
                    widget.setChecked(bool(value))

            widget.blockSignals(False)

    # Get settings from childs
    def getSettings(self) -> dict:
        # Return settings
        return {            
            "themeComboBox": self.ui.themeComboBox.currentText(),
            "stylesheetComboBox": self.ui.stylesheetComboBox.currentText(),
            "fontComboBox": self.ui.fontComboBox.currentText(),
            "fontSizeComboBox": self.ui.fontSizeComboBox.currentText(),
            "checkUpdatesComboBox": self.ui.checkUpdatesComboBox.currentText()
        }
    
    '''
    Marking as not saved.
    '''

    # Automatically discovers input widgets and connects their change signals to the dirty state tracker.
    def _connectChangesTracking(self) -> None:
        container = self.ui.generalScrollContent
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
        self.isSaved = False#

