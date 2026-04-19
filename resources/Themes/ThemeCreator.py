# ThemeCreator.py

# Importing system files
import re
import json
import os

from PySide6.QtWidgets import QDialog, QColorDialog, QMessageBox, QFileDialog # type: ignore
from PySide6 import QtCore, QtGui # type: ignore

from Application.QtFiles.ThemeCreator import Ui_ThemeCreator
from Application.QtFiles.ThemePreview import Ui_ThemePreview

# Main class ThemeCreator
class ThemeCreator(QDialog):
        
    # Constructor
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
        self.custom_theme = {state: {} for state in ["Active", "Inactive", "Disabled"]}

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
        self.ui.btn_export.clicked.connect(self._export_theme)
        self.ui.btn_import.clicked.connect(self._importTheme)

    # Make icon function
    def _makeIcon(self, color: QtGui.QColor) -> QtGui.QIcon:
        pixmap = QtGui.QPixmap(24, 14)
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
        
        item = selectedItem[0]
        roleName = item.text(0)
        currentState = self.ui.cb_state.currentText().split(" ")[0]

        currentHex = item.text(1)
        initialColor = QtGui.QColor(currentHex) if currentHex else QtGui.QColor(QtCore.Qt.GlobalColor.white)

        color = QColorDialog.getColor(initialColor, self, f"Pick Color for {roleName} ({currentState})")

        # Check if color is valid
        if color.isValid():
            # Get new color
            newHex = color.name().upper()
            
            self.custom_theme[currentState][roleName] = color
            
            # Actualize Ui of table
            item.setText(1, newHex) 
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
            if roleName in self.custom_theme[currentState]:
                # Get color
                color = self.custom_theme[currentState][roleName]

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
        if roleName in self.custom_theme[currentState]:
            # Remove
            del self.custom_theme[currentState][roleName]

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
            self.previewWindow.setPalette(self._buildPalette())

    # Building palette
    def _buildPalette(self) -> QtGui.QPalette:
        # Create new palette
        palette = QtGui.QPalette()
        
        # Set state map
        stateMap = {
            "Active": QtGui.QPalette.ColorGroup.Active,
            "Inactive": QtGui.QPalette.ColorGroup.Inactive,
            "Disabled": QtGui.QPalette.ColorGroup.Disabled
        }
        
        # Browse all states names and roles
        for stateName, roles in self.custom_theme.items():
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
        currentPalette = self._buildPalette()

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

    # TODO: Import 
    def _importTheme(self) -> None:
        # Open file dialog and return path
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import theme",
            "theme", 
            "JSON File (*.json);;Qt Stylesheet (*.qss);;Python Dict (*.py)"
        )

        # Get type
        _, extension = os.path.splitext(file_path)
        type = extension.lower()
        
        # Open file
        with open(file_path, "r") as theme:
            # Get data
            data = theme.readlines()

            # Close file
            theme.close()

        # Reset table
        self._updateTableFromData()

        # Update preview
        self._applyToPreview()

    # Export as json
    def _export_as_json(self, file_path) -> None:
        # Parsed data
        export_data = {}

        # Groups
        for group, roles in self.custom_theme.items():
            # Empty dict for each group
            export_data[group] = {} 
            
            # Roles and colors
            for role, color in roles.items():
                # Make string from QColor
                hex_color = color.name().upper()
                
                # Save to new dict
                export_data[group][role] = hex_color

        # Open file
        with open(file_path, "w") as theme:
            # Write it 
            json.dump(export_data, theme, indent=4)

    # Export as *.py
    def _export_as_py(self, file_path) -> None:
        # Parsed data
        export_data = {}

        # Groups
        for group, roles in self.custom_theme.items():
            # Empty dict for each group
            export_data[group] = {} 
            
            # Roles and colors
            for role, color in roles.items():
                # Make string from QColor
                hex_color = color.name().upper()
                
                # Save to new dict
                export_data[group][role] = hex_color

        file_content = f"""from PySide6.QtGui import QPalette, QColor

THEME_DATA = {export_data}

def get_palette():
    palette = QPalette()
    groups = {{
        "Active": QPalette.ColorGroup.Active,
        "Inactive": QPalette.ColorGroup.Inactive,
        "Disabled": QPalette.ColorGroup.Disabled
    }}
    for group_name, roles in THEME_DATA.items():
        qt_group = groups.get(group_name)
        for role_name, hex_color in roles.items():
            try:
                qt_role = getattr(QPalette.ColorRole, role_name)
                palette.setColor(qt_group, qt_role, QColor(hex_color))
            except AttributeError:
                continue
    return palette

def apply_theme(app):
    app.setPalette(get_palette())
        """

        # Open file
        with open(file_path, "w") as theme:
            # Write it 
            theme.write(file_content)

    # Export as *.qss
    def _export_as_qss(self, file_path) -> None:
        # Line start
        lines = ["#ThemeData {"]
        
        # Groups
        for group, roles in self.custom_theme.items():
            group_name = group.lower()
            # Roles, colors
            for role, color in roles.items():
                hex_val = color.name().upper()
                # Line with property
                lines.append(f"    qproperty-{group_name}-{role.lower()}: {hex_val};")
        
        lines.append("}")

        # Create full text
        full_text = "\n".join(lines)

        # Open file
        with open(file_path, "w") as theme:
            theme.write(str(full_text))

    # Save theme method
    def _export_theme(self) -> None:
        # Get decode type
        decode_type = self.ui.cb_format.currentText()

        # Open file dialog and return path
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save theme",
            "resources/Themes/theme", 
            str(decode_type)
        )

        # Close dialog and return empty string
        if not file_path:
            return
        
        # Repair types
        if "(*.json)" in decode_type and not file_path.endswith(".json"):
            file_path += ".json"
        elif "(*.qss)" in decode_type and not file_path.endswith(".qss"):
            file_path += ".qss"
        elif "(*.py)" in decode_type and not file_path.endswith(".py"):
            file_path += ".py"

        try:
            # Check if its is json, python or qss
            if "json" in decode_type:
                self._export_as_json(file_path)
            elif "qss" in decode_type:
                self._export_as_qss(file_path)
            elif "py" in decode_type:
                self._export_as_py(file_path)
        except Exception as e:
            print(e) 