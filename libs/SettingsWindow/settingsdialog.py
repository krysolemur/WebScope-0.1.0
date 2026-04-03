# settingswindow.py

# Module for managing settings window

# Importing system files
import sys
import os

from PySide6.QtWidgets import QDialog, QSlider, QComboBox, QWidget, QCheckBox, QFontDialog, QColorDialog # type: ignore
from PySide6.QtCore import QSignalBlocker, QSize, Qt # type: ignore
from PySide6.QtGui import QIcon, QPixmap # type: ignore

# Importing program files
from libs.Logging.logging import Logging
from resources.Themes.theme import Theme

from libs.QtGuiFiles.PyFiles.SettingsDialog import Ui_SettingsDialog
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog
from libs.QtGuiFiles.PyFiles.StyleDialog import Ui_styleDialog

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
        self.ui.themeAddButton.clicked.connect(self.theme.getTheme)

        # Resize
        self.resize(660, 528)

        '''
        Source code buttons actions.
        '''

        # Html elements style button
        self.ui.htmlElementsButton.clicked.connect(lambda: self.ui.htmlElementsButton.setStyleSheet(self._stylePicker().strip()))

        # Html elements style button
        self.ui.htmlAtributsButton.clicked.connect(lambda: self.ui.htmlAtributsButton.setStyleSheet(self._stylePicker().strip()))

        # Html elements style button
        self.ui.atributsValuesButton.clicked.connect(lambda: self.ui.atributsValuesButton.setStyleSheet(self._stylePicker().strip()))

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
                elif isinstance(widget, QCheckBox):
                    # Load their value for checkbox
                    widget.setChecked(bool(value))

    # Get value of all settings childs, make dictonary from it and overwrite config.json.
    def _saveSettingsAction(self) -> None:
        # Settings
        settings = {
            "askOnCloseComboBox": self.ui.askOnCloseComboBox.currentText(),
            "themeComboBox": self.ui.themeComboBox.currentText(),
            "stylesheetComboBox": self.ui.stylesheetComboBox.currentText(),
            "fontComboBox": self.ui.fontComboBox.currentText(),
            "fontSizeSlider": self.ui.fontSizeSlider.value(),
            "checkUpdatesComboBox": self.ui.checkUpdatesComboBox.currentText(),
            "htmlElementsCheckBox": self.ui.htmlElementsCheckBox.isChecked(),
            "htmlAtributsCheckBox": self.ui.htmlAtributsCheckBox.isChecked(),
            "atributsValuesCheckBox": self.ui.atributsValuesCheckBox.isChecked()
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

    # Logic for a custom style picker dialog designed for HTML text elements.
    def _stylePicker(self) -> str:
        '''
        Initializes and manages a sub-dialog for picking text styles.
        Contains nested helper functions to handle UI updates and color selection.
        '''

        # Nested function to refresh the visual preview label based on current selections.
        def _updatePreview() -> None:
            # Retrieve the stored foreground color or default to black if not set.
            fg = getattr(self, 'current_fg', 'black')

            # Retrieve the stored background color or default to transparent.
            bg = getattr(self, 'current_bg', 'transparent')

            # Determine font weight based on the toggle state of the bold button.
            weight = "bold" if styleDialogUi.boldButton.isChecked() else "normal"

            # Determine font style based on the toggle state of the italic button.
            style = "italic" if styleDialogUi.italicButton.isChecked() else "normal"

            # Determine text decoration based on the toggle state of the underline button.
            under = "underline" if styleDialogUi.underlineButton.isChecked() else "none"

            # Get the currently selected index from the text case combo box.
            case_index = styleDialogUi.caseComboBox.currentIndex()

            # Initialize text transform as none and update based on index selection.
            transform = "none"
            # Check if the user selected the Uppercase option (Index 1).
            if case_index == 1:
                # Apply uppercase transformation.
                transform = "uppercase"
            # Check if the user selected the Lowercase option (Index 2).
            elif case_index == 2:
                # Apply lowercase transformation.
                transform = "lowercase"
            # Check if the user selected the Capitalize option (Index 3).
            elif case_index == 3:
                # Apply capitalization to the first letter of each word.
                transform = "capitalize"

            # Apply the generated CSS-like stylesheet to the preview label.
            styleDialogUi.exampleTextLabel.setStyleSheet(f"""
                color: {fg};
                background-color: {bg};
                font-weight: {weight};
                font-style: {style};
                text-decoration: {under};
                text-transform: {transform};
            """)

            # Evaluate if any styling attribute differs from its default state.
            has_changes = (fg != 'black' or bg != 'transparent' or 
                           styleDialogUi.boldButton.isChecked() or 
                           styleDialogUi.italicButton.isChecked() or 
                           styleDialogUi.underlineButton.isChecked() or
                           styleDialogUi.caseComboBox.currentIndex() != 0)
            
            # Toggle the reset button's availability based on the presence of changes.
            styleDialogUi.resetButton.setEnabled(has_changes)

        # Nested function to open the system color picker and store the result.
        def _handleColorChange(button) -> None:
            # Invoke the standard Qt color dialog to let the user pick a color.
            color = QColorDialog.getColor()

            # Verify that the user confirmed the selection and didn't cancel.
            if color.isValid():
                # Determine if the foreground button triggered the change.
                if button == styleDialogUi.foregroundButton:
                    # Store the selected hex color as the current foreground.
                    self.current_fg = color.name()
                # Determine if the background button triggered the change.
                elif button == styleDialogUi.backgroundButton:
                    # Store the selected hex color as the current background.
                    self.current_bg = color.name()
                
                # Refresh the preview label to reflect the new color selection.
                _updatePreview()

        # Function to extract the CSS stylesheet from the preview label and return it as a string.
        def _encodeStyle() -> str:
            # Store the resulting CSS string into the instance variable before closing.
            self.css = styleDialogUi.exampleTextLabel.styleSheet()

            # Close the dialog and return the QDialog.Accepted code to the caller.
            styleDialog.accept()

            # Return the generated CSS for internal function usage.
            return self.css
        
        # Nested function to clear all custom style selections and refresh the UI.
        def _resetStyles() -> None:
            # Revert color variables to their default states.
            self.current_fg = 'black'
            self.current_bg = 'transparent'

            # Uncheck all styling toggle buttons.
            styleDialogUi.boldButton.setChecked(False)
            styleDialogUi.italicButton.setChecked(False)
            styleDialogUi.underlineButton.setChecked(False)

            # Reset the text case selection to the first index (None).
            styleDialogUi.caseComboBox.setCurrentIndex(0)

            # Update the preview label to reflect the cleared styles.
            _updatePreview()
            
        '''
        Dialog initialization, UI loading, and widget setup.
        '''

        # Create a new QDialog instance with the main window as its parent.
        styleDialog = QDialog(self)

        # Instantiate the generated UI layout for the style picker.
        styleDialogUi = Ui_styleDialog()

        # Apply the layout and widgets to the newly created dialog instance.
        styleDialogUi.setupUi(styleDialog)

        # Trigger initial preview update to show default settings.
        _updatePreview()

        '''
        Configuring dialog window properties like geometry and titles.
        '''

        # Prevent the user from shrinking the window below its calculated size hint.
        styleDialog.setMinimumSize(styleDialog.sizeHint())

        # Set the initial dimensions of the dialog based on its layout needs.
        styleDialog.resize(styleDialog.sizeHint())

        # Define the title displayed in the window's title bar.
        styleDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Style picker")

        '''
        Establishing signal and slot connections for interactive widgets.
        '''

        # Trigger color selection for the text foreground on button click.
        styleDialogUi.foregroundButton.clicked.connect(lambda: _handleColorChange(styleDialogUi.foregroundButton))

        # Trigger color selection for the text background on button click.
        styleDialogUi.backgroundButton.clicked.connect(lambda: _handleColorChange(styleDialogUi.backgroundButton))     

        # Update the live preview whenever the bold toggle is clicked.
        styleDialogUi.boldButton.clicked.connect(_updatePreview)        

        # Update the live preview whenever the italic toggle is clicked.
        styleDialogUi.italicButton.clicked.connect(_updatePreview)      

        # Update the live preview whenever the underline toggle is clicked.
        styleDialogUi.underlineButton.clicked.connect(_updatePreview)      

        # Update the live preview whenever the text case selection changes.
        styleDialogUi.caseComboBox.currentIndexChanged.connect(_updatePreview)

        # Execute the encoding logic when the user confirms with the OK button.
        styleDialogUi.okButton.clicked.connect(_encodeStyle)

        # Trigger the style reset logic whenever the reset button is clicked.
        styleDialogUi.resetButton.clicked.connect(_resetStyles)

        # Display the dialog as a modal window and capture the return result.
        result = styleDialog.exec()

        # Evaluate if the dialog was closed via the OK button (Accepted).
        if result == QDialog.Accepted:
            # Return the CSS string captured during the encoding process.
            return getattr(self, 'css', "")
        
        # Return an empty string if the user cancelled or closed the dialog.
        return ""

    '''
    Public functions.
    '''

    # Overriding the default Qt close event to handle unsaved changes.
    def closeEvent(self, event) -> None:
        '''
        Handles the window closure logic by checking if settings are saved.
        If changes are pending, it prompts the user with a confirmation dialog.
        '''

        # Check the boolean flag that tracks if current settings are saved
        if self.isSaved:
            # Log an informational message about closing the window
            self.printi(msg="Closing settings window")

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
            self.printi(msg="Saving and quitting...")

            # Execute the internal logic to write settings to storage
            self._saveSettingsAction() 

            # Allow the main window close event to proceed
            event.accept() 

        # Evaluate if the user chose to 'Close without saving'
        elif result == QDialog.Rejected:
            # Log that the window is closing and changes are being discarded
            self.printi(msg="Quitting without saving")

            # Allow the main window close event to proceed despite lack of saving
            event.accept()

        # Handle cases where the user closes the dialog without a choice (e.g., Esc)
        else:
            # Cancel the window closure to keep the settings window open
            event.ignore()