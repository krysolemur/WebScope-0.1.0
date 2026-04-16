# ThemeCreator.py

# Importing system files
import json
import os

from PySide6.QtWidgets import QDialog, QColorDialog, QMessageBox, QFileDialog # type: ignore
from PySide6 import QtCore, QtGui # type: ignore

# Importing program files
from Application.QtFiles.ThemeCreator import Ui_ThemeCreator
from Application.QtFiles.ThemePreview import Ui_ThemePreview

# Main class ThemeCreator
class ThemeCreator(QDialog):
        
    # Initiator
    def __init__(self) -> None:
        
        # Init parents
        super().__init__()

        # Color Role mapping
        self.roleMapping = {
            "Window": QtGui.QPalette.ColorRole.Window,
            "WindowText": QtGui.QPalette.ColorRole.WindowText,
            "Base": QtGui.QPalette.ColorRole.Base,
            "AlternateBase": QtGui.QPalette.ColorRole.AlternateBase,
            "Text": QtGui.QPalette.ColorRole.Text,
            "Button": QtGui.QPalette.ColorRole.Button,
            "ButtonText": QtGui.QPalette.ColorRole.ButtonText,
            "BrightText": QtGui.QPalette.ColorRole.BrightText,
            "Light": QtGui.QPalette.ColorRole.Light,
            "Midlight": QtGui.QPalette.ColorRole.Midlight,
            "Dark": QtGui.QPalette.ColorRole.Dark,
            "Mid": QtGui.QPalette.ColorRole.Mid,
            "Shadow": QtGui.QPalette.ColorRole.Shadow,
            "Highlight": QtGui.QPalette.ColorRole.Highlight,
            "HighlightedText": QtGui.QPalette.ColorRole.HighlightedText,
            "Link": QtGui.QPalette.ColorRole.Link,
            "LinkVisited": QtGui.QPalette.ColorRole.LinkVisited,
            "PlaceholderText": QtGui.QPalette.ColorRole.PlaceholderText,
            "ToolTipBase": QtGui.QPalette.ColorRole.ToolTipBase,
            "ToolTipText": QtGui.QPalette.ColorRole.ToolTipText
        }

        # Create empty default palette
        self.customPalette = {state: {} for state in ["Active", "Inactive", "Disabled"]}

        # Preview window
        self.previewWindow = None

        # Load Ui
        self.ui = Ui_ThemeCreator()
        
        # Setup ui
        self.ui.setupUi(self)

        # Actions
        self.ui.btn_full_preview.clicked.connect(self._showPreview)
        self.ui.btn_set_color.clicked.connect(self._colorPicker)
        self.ui.cb_state.currentIndexChanged.connect(self._updateTableFromData)
        self.ui.btn_import.clicked.connect(self._resetRole)
        self.ui.btn_export.clicked.connect(self._saveTheme)

        # Exec dialog
        self.exec()

    # Make icon function
    def _makeIcon(self, color: QtGui.QColor) -> QtGui.QIcon:
        # Create pixmap
        pixmap = QtGui.QPixmap(24, 14)

        # Fill with color
        pixmap.fill(color)

        # Return pixmap as icon
        return QtGui.QIcon(pixmap)

    # Pick color function
    def _colorPicker(self) -> None:
        # Get selected item
        selectedItem = self.ui.tw_palette_roles.selectedItems()

        # Checkk selected
        if not selectedItem:
            return
        
        # Get item
        item = selectedItem[0]

        # Get role name
        roleName = item.text(0)

        # And current state
        currentState = self.ui.cb_state.currentText().split(" ")[0] # Získá 'Active', 'Inactive' nebo 'Disabled'

        # Default color dialog color
        currentHex = item.text(1)

        # And initial color
        initialColor = QtGui.QColor(currentHex) if currentHex else QtGui.QColor(QtCore.Qt.GlobalColor.white)

        # Open QColorDialog
        color = QColorDialog.getColor(initialColor, self, f"Pick Color for {roleName} ({currentState})")

        # Check if color is valid
        if color.isValid():
            # Get new color
            newHex = color.name().upper()
            
            # Dave to dict structure
            self.customPalette[currentState][roleName] = color
            
            # Actualize Ui of table
            item.setText(1, newHex) #
            
            # Setin pixmap as a color for item
            item.setIcon(2, self._makeIcon(color))

            # Apply to preview
            self._applyToPreview()
            
    # Update table
    def _updateTableFromData(self) -> None:
        # Get current state
        currentState = self.ui.cb_state.currentText().split(" ")[0]

        # Get root
        root = self.ui.tw_palette_roles.invisibleRootItem()

        # Block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(False)

        # Browse all childs
        for i in range(root.childCount()):
            # Get item
            item = root.child(i)
            
            # Get role name
            roleName = item.text(0)
            
            # Get roleName
            if roleName in self.customPalette[currentState]:
                # Get color
                color = self.customPalette[currentState][roleName]

                # Set text from color name
                item.setText(1, color.name().upper())

                # Set icon
                item.setIcon(2, self._makeIcon(color))
            else:
                # Set none text
                item.setText(1, "")

                # Set none icon
                item.setIcon(2, QtGui.QIcon())

        # Update preview
        self._applyToPreview

        # Cancle block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(True)

    # Reset role function
    def _resetRole(self) -> None:
        """Resetuje vybranou barevnou roli pro aktuální stav."""
        # Get selected
        selectedItem = self.ui.tw_palette_roles.selectedItems()

        # Check selected
        if not selectedItem:
            return

        # Get item
        item = selectedItem[0]

        # Get role name
        roleName = item.text(0)
        
        # Get current state
        currentState = self.ui.cb_state.currentText().split(" ")[0]


        # Removing from data structure
        if roleName in self.customPalette[currentState]:
            # Remove
            del self.customPalette[currentState][roleName]

        # Clear table
        item.setText(1, "")           

        # Icon
        item.setIcon(2, QtGui.QIcon()) 
        
        # Actualize preview
        self._applyToPreview()

    # Applying to preview
    def _applyToPreview(self) -> None:
        # Check if it has that atribute
        if hasattr(self, 'previewWindow') and self.previewWindow is not None:
            # Set palette
            self.previewWindow.setPalette(self.build_palette())

    # Building palette
    def build_palette(self) -> QtGui.QPalette:
        # Create new palette
        palette = QtGui.QPalette()
        
        # Set state map
        stateMap = {
            "Active": QtGui.QPalette.ColorGroup.Active,
            "Inactive": QtGui.QPalette.ColorGroup.Inactive,
            "Disabled": QtGui.QPalette.ColorGroup.Disabled
        }
        
        # Browse all states names and roles
        for stateName, roles in self.customPalette.items():
            # Get group
            group = stateMap[stateName]

            # Browse all role name and their colors
            for roleName, color in roles.items():
                # If is role name in mapping
                if roleName in self.roleMapping:
                    # Set color
                    palette.setColor(group, self.roleMapping[roleName], color)
        
        # Return palette
        return palette
    
    # Show preview function
    def _showPreview(self) -> None:        
        # Check if window exists
        if not hasattr(self, 'previewWindow') or self.previewWindow is None:
            try:
                # Create dialog
                self.previewWindow = QDialog(self)

                # Load ui
                self.previewUi = Ui_ThemePreview()

                # Setup ui
                self.previewUi.setupUi(self.previewWindow)
            except Exception as e:
                # Show error
                QMessageBox.critical(self, "Error", f"Could not load Preview Dialog: {e}")
                return

        # Create current palette
        currentPalette = self.build_palette()

        # Apply palette
        # Teď už voláme setPalette na QDialog, který tuto metodu má
        self.previewWindow.setPalette(currentPalette)
        
        # Repain preview
        self.previewWindow.update()

        # Show window is its hiden
        if not self.previewWindow.isVisible():
            self.previewWindow.show()
        else:
            # If is open, just raise it and set as active window
            self.previewWindow.raise_()
            self.previewWindow.activateWindow()

    # Export 
    def _decode(self, palette, type) -> str:
        print(f"decoded as {type}")

    # Save theme method
    def _saveTheme(self) -> None:
        decodeType = self.ui.cb_format.currentText()

        # Open file dialog and return path
        filePath, _ = QFileDialog.getSaveFileName(
            self,
            "Save Theme",
            "theme.json", 
            str(decodeType)
        )

        # Close dialog and return empty string
        if not filePath:
            return

        try:
            # Open file
            with open(filePath, "w") as theme:
                None
        except Exception as e:
            None
