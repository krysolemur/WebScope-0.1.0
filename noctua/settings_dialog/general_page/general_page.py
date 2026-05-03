# generalpage.py

from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QWidget, QSpinBox, QFontComboBox, QFileDialog # type: ignore
from PySide6.QtGui import QFont # type: ignore

from noctua.ui_gen.GeneralPage import Ui_GeneralPage
from noctua.context import ctx

# Main class GeneralPage
class GeneralPage(QWidget):

    # Initiator
    def __init__(self, app) -> None:

        # Init apps
        super().__init__(app)

        # Load page Ui
        self.ui = Ui_GeneralPage()

        # Setup Ui 
        self.ui.setupUi(self)

        # ThemeManager
        # self.ThemeManager = ctx.ThemesManager

        # Load settings
        self.load_settings(ctx.config.get("GeneralPage"))

        # Saved variable
        self.isSaved = True

        # Connect tracking changes for all widgets
        self._connectChangesTracking()
                
        # TODO: Add all themes to theme combobox
        # self.ui.themeComboBox.addItems(self.theme.themes())

        # Add theme 
        self.ui.btn_gen_theme.clicked.connect(self._addTheme)

        # TODO: Add stylesheet
        #self.ui.btn_gen_stylesheet.clicked.connect(self._addStylesheet)

    # TODO: Add theme function
    def _addTheme(self) -> None:
        # Get path
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Add theme",  
            "",          
            "Python Files (*.py);;JSON Files (*.json);;Qt Style Sheets (*.qss);;All Files (*)"
        )

        # Check path 
        if not filePath:
            return
        
        # Add path
        if not self.ThemeManager.addTheme(path=filePath):
            print("error")

    # TODO: Add stylesheet
    # def _addStylesheet(self) -> None:
    #     # Get path
    #     filePath, _ = QFileDialog.getOpenFileName(
    #         self,
    #         "Add stylesheet",  
    #         "",          
    #         "Qt Style Sheets (*.qss);;All Files (*)"
    #     )

    #     # Check path 
    #     if not filePath:
    #         return
        
    #     # Add path
    #     if not StyleManager.addStyle(path=filePath):
    #         print("error")

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

            widget.blockSignals(True)

            # Checkboxy
            if isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))

            # ComboBoxy
            elif isinstance(widget, QComboBox) and not isinstance(widget, QFontComboBox):
                index = widget.findText(str(value))
                if index >= 0:
                    widget.setCurrentIndex(index)
            
            # Fonts
            elif isinstance(widget, QFontComboBox):
                widget.setCurrentFont(QFont(str(value)))

            # 4. SpinBoxy 
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except (ValueError, TypeError):
                    pass

            # 5. Slidery
            elif isinstance(widget, QSlider):
                widget.setValue(int(value))

            # 6. PushButtony
            elif isinstance(widget, QPushButton):
                if widget.isCheckable():
                    widget.setChecked(bool(value))

            widget.blockSignals(False)

    # Get settings from childs
    def get_settings(self) -> dict:
        return {
            # Appearance
            "cb_gen_theme": self.ui.cb_gen_theme.currentText(),
            "fcb_gen_font": self.ui.fcb_gen_font.currentFont().family(),
            "cb_gen_font_size": self.ui.cb_gen_font_size.currentText(),
            
            # Advanced
            "sb_adv_autosave_interval": self.ui.sb_adv_autosave_interval.value(),
            "chk_adv_gpu": self.ui.chk_adv_gpu.isChecked(),
            "cb_adv_startup": self.ui.cb_adv_startup.currentText(),
            
            # System
            "chk_sys_updates": self.ui.chk_sys_updates.isChecked(),
            "chk_sys_telemetry": self.ui.chk_sys_telemetry.isChecked(),
            "cb_sys_lang": self.ui.cb_sys_lang.currentText()
        }

    # Automatically discovers input widgets and connects their change signals to the dirty state tracker.
    def _connectChangesTracking(self) -> None:
        container = self.ui.sa_general
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

