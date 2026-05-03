# sourcepage.py

# Importing system files
import re 

from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QDialog, QColorDialog, QWidget # type: ignore
from PySide6.QtCore import QSignalBlocker # type: ignore
from PySide6.QtGui import QColor # type: ignore

# Importing program files
from noctua.ui_gen.SourcePage import Ui_sourcePage

# Class with color picker
class SourcePage(QWidget):

    # Initiator
    def __init__(self, app) -> None:

        # Init app
        super().__init__(app)

        # Load page
        self.ui = Ui_sourcePage()

        # Setup ui
        self.ui.setupUi(self)

        # Saved
        self.isSaved = True

        # Set tracking
        self._connectChangesTracking()

    '''
    Style methods.
    '''

    '''
    Settings methods.
    '''

    # Load settings function
    def load_settings(self, settings) -> None:
        # Save settings
        self.settings = settings

        # Browse all keys and their values
        for key, value in settings.items():
            # Get widget by name
            widget = getattr(self.ui, key, None)

            # If widget is None, skip
            if widget is None:
                continue
            
            # Block signals
            widget.blockSignals(True)

            # Check instances
            if isinstance(widget, QCheckBox):
                # Set value for checkbox
                widget.setChecked(bool(value))
            elif isinstance(widget, QPushButton):
                # Check if button is checkable
                if widget.isCheckable():
                    # Load style
                    widget.style = self.settings.get(widget.objectName())      

            # Block signals
            widget.blockSignals(False)

        
        # Load style
        # self._loadStyle()

    # Get settings from childs
    def get_settings(self) -> dict:
        # Tady sestavíme slovník přesně podle jmen v UI a v configu
        return {
            # Styly pro jednotlivé typy kódu
            "btn_sel_tags": self.ui.btn_sel_tags.style if hasattr(self.ui.btn_sel_tags, 'style') else {},
            "btn_sel_attrs": self.ui.btn_sel_attrs.style if hasattr(self.ui.btn_sel_attrs, 'style') else {},
            "btn_sel_strings": self.ui.btn_sel_strings.style if hasattr(self.ui.btn_sel_strings, 'style') else {},
            "btn_sel_comments": self.ui.btn_sel_comments.style if hasattr(self.ui.btn_sel_comments, 'style') else {},
            
            # Pokročilé nastavení editoru (hodnoty z checkboxů a spinboxů)
            "chk_auto_close": self.ui.chk_auto_close.isChecked(),
            "chk_line_numbers": self.ui.chk_line_numbers.isChecked(),
            "chk_word_wrap": self.ui.chk_word_wrap.isChecked(),
            "chk_format_save": self.ui.chk_format_save.isChecked(),
            
            # Pokud jsi přidal i výběr transformace textu
            "cb_style_transform": self.ui.cb_style_transform.currentText()
        }
    
    '''
    Marking as not saved.
    '''

    # Automatically discovers input widgets and connects their change signals to the dirty state tracker.
    def _connectChangesTracking(self) -> None:
        container = self.ui.sourceCodeScrollContent
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
            # # Check if is checkabel
            # if button.isCheckable():
            #     # Connect the toggle signal to the dirty state tracker for checkable buttons.
            #     button.clicked.connect(self._markAsDirty)
            None

    # Function that change isSaved status if somethings is saved.
    def _markAsDirty(self) -> None:
        # Change saved status
        self.isSaved = False
