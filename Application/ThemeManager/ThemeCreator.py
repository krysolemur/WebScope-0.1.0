# ThemeCreator.py

# Importing system files
from pathlib import Path
import importlib.util
import re
import json
import os

from PySide6.QtWidgets import QDialog, QColorDialog, QMessageBox, QFileDialog # type: ignore
from PySide6.QtGui import QColor, QPalette, QIcon, QPixmap # type: ignore
from PySide6.QtCore import Qt # type: ignore

from Application.QtFiles.ThemeCreator import Ui_ThemeCreator
from Application.QtFiles.ThemePreview import Ui_ThemePreview

# Main class ThemeCreator
class ThemeCreator(QDialog):
        
    # Constructor
    def __init__(self) -> None:
        
        # Init parents
        super().__init__()

        # Color Role mapping
        self.role_mapping = {
            "Window": QPalette.ColorRole.Window,
            "WindowText": QPalette.ColorRole.WindowText,
            "Base": QPalette.ColorRole.Base,
            "AlternateBase": QPalette.ColorRole.AlternateBase,
            "Text": QPalette.ColorRole.Text,
            "Button": QPalette.ColorRole.Button,
            "ButtonText": QPalette.ColorRole.ButtonText,
            "BrightText": QPalette.ColorRole.BrightText,
            "Light": QPalette.ColorRole.Light,
            "Midlight": QPalette.ColorRole.Midlight,
            "Dark": QPalette.ColorRole.Dark,
            "Mid": QPalette.ColorRole.Mid,
            "Shadow": QPalette.ColorRole.Shadow,
            "Highlight": QPalette.ColorRole.Highlight,
            "HighlightedText": QPalette.ColorRole.HighlightedText,
            "Link": QPalette.ColorRole.Link,
            "LinkVisited": QPalette.ColorRole.LinkVisited,
            "PlaceholderText": QPalette.ColorRole.PlaceholderText,
            "ToolTipBase": QPalette.ColorRole.ToolTipBase,
            "ToolTipText": QPalette.ColorRole.ToolTipText
        }

        # Create empty default palette
        self.custom_theme = {
            "Active": {}, 
            "Inactive": {},
            "Disabled": {}
        }

        # Preview window instance
        self.preview_window = None

        # Load Ui
        self.ui = Ui_ThemeCreator()
        
        # Setup ui
        self.ui.setupUi(self)

        # Actions
        self.ui.btn_full_preview.clicked.connect(self._show_preview)
        self.ui.btn_set_color.clicked.connect(self._color_picker)
        self.ui.btn_reset.clicked.connect(self._reset_role)
        self.ui.btn_export.clicked.connect(self._export_theme)
        self.ui.btn_import.clicked.connect(self._import_theme)
        self.ui.cb_state.currentIndexChanged.connect(self._update_table)

    # Make icon from pixmap
    def _make_icon(self, color: QColor) -> QIcon:
        # Create pixmap
        pixmap = QPixmap(24, 14)
        pixmap.fill(color)

        # Return pixmap as icon
        return QIcon(pixmap)

    # Show color dialog
    def _color_picker(self) -> None:
        # Get selected item
        selected_item = self.ui.tw_palette_roles.selected_items()

        # Check selected
        if not selected_item:
            return
        
        # Get item, role_name and current state
        item = selected_item[0]
        role_name = item.text(0)
        current_state = self.ui.cb_state.currentText().split(" ")[0]

        # Get Hex and parse it to QColor
        current_hex = item.text(1)
        initialColor = QColor(current_hex) if current_hex else QColor(Qt.GlobalColor.white)

        # Show dialog with color
        color = QColorDialog.getColor(initialColor, self, f"Pick Color for {role_name} ({current_state})")

        # Check if color is valid
        if color.isValid():
            # Get new color
            new_hex = color.name().upper()
            
            # Save it into dict
            self.custom_theme[current_state][role_name] = color
            
            # Actualize Ui of table
            item.setText(1, new_hex) 
            item.setIcon(2, self._make_icon(color))

            # Apply to preview
            self._apply_to_preview()
            
    # Update table from actual data
    def _update_table(self) -> None:
        # Get current state
        current_state = self.ui.cb_state.currentText().split(" ")[0]

        # Get root
        root = self.ui.tw_palette_roles.invisibleRootItem()

        # Block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(False)

        # Browse all childs
        for i in range(root.childCount()):
            # Get item and role name
            item = root.child(i)
            role_name = item.text(0)
            
            # Get role_name
            if role_name in self.custom_theme[current_state]:
                # Get color
                color = self.custom_theme[current_state][role_name]

                # Set text from color name and icon from pixmap
                item.setText(1, color.name().upper())
                item.setIcon(2, self._make_icon(color))
            else:
                # Set none text and icon
                item.setText(1, "")
                item.setIcon(2, QIcon())

        # Update preview
        self._apply_to_preview

        # Cancle block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(True)

    # Reset role color
    def _reset_role(self) -> None:
        # Get selected
        selected_item = self.ui.tw_palette_roles.selected_items()

        # Check selected
        if not selected_item:
            return

        # Get item, role name, current state
        item = selected_item[0]
        role_name = item.text(0)
        current_state = self.ui.cb_state.currentText().split(" ")[0]


        # Removing from data structure
        if role_name in self.custom_theme[current_state]:
            # Clear
            del self.custom_theme[current_state][role_name]

        # Clear table and icon
        item.setText(1, "")           
        item.setIcon(2, QIcon()) 
        
        # Actualize preview
        self._apply_to_preview()

    # Applying to preview
    def _apply_to_preview(self) -> None:
        # Check if it has that atribute
        if hasattr(self, 'preview_window') and self.preview_window is not None:
            # Set palette
            self.preview_window.setPalette(self._build_palette())

    # Building palette from actual palette
    def _build_palette(self) -> QPalette:
        # Create new palette
        palette = QPalette()
        
        # Set state map
        state_map = {
            "Active": QPalette.ColorGroup.Active,
            "Inactive": QPalette.ColorGroup.Inactive,
            "Disabled": QPalette.ColorGroup.Disabled
        }
        
        # Browse all states names and roles
        for stateName, roles in self.custom_theme.items():
            # Get group
            group = state_map[stateName]

            # Browse all role name and their colors
            for role_name, color in roles.items():
                # If is role name in mapping
                if role_name in self.role_mapping:
                    # Set color
                    palette.setColor(group, self.role_mapping[role_name], color)
        
        # Return palette
        return palette
    
    # Show preview window
    def _show_preview(self) -> None:
        # Check if window exists
        if not hasattr(self, 'preview_window') or self.preview_window is None:
            try:
                # Create dialog
                self.preview_window = QDialog(self)

                # Load ui
                self.previewUi = Ui_ThemePreview()

                # Setup ui
                self.previewUi.setupUi(self.preview_window)
            except Exception as e:
                # Show error
                QMessageBox.critical(self, "Error", f"Could not load Preview Dialog: {e}")
                return

        # Create current palette and set it
        current_palette = self._build_palette()
        self.preview_window.setPalette(current_palette)
        
        # Update window
        self.preview_window.update()

        # Show window on top
        if not self.preview_window.isVisible():
            self.preview_window.show()
        else:
            # If is open, just raise it and set as active window
            self.preview_window.raise_()
            self.preview_window.activateWindow()

    # Import method
    def _import_theme(self) -> None:
        # Open file dialog 
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import theme",
            "resources/Themes", 
            "JSON File (*.json);;Qt Stylesheet (*.qss);;Python Dict (*.py)"
        )

        # Check file path
        if not file_path:
            return

        # Get type
        _, extension = os.path.splitext(file_path)
        type = extension.lower()

        # Import palette
        try:
            if "json" in type:
                self._import_from_json(file_path)
            elif "qss" in type:
                self._import_from_qss(file_path)
            elif "py" in type:
                self._import_from_py(file_path)
        except Exception as e:
            print(e)

        # Reset table
        self._update_table()

        # Update preview
        self._apply_to_preview()

    # Import from *.json
    def _import_from_json(self, file_path) -> None:
        # Open file
        with open(file_path, "r") as theme:
            exported_data = json.load(theme)

        # Groups
        for group, roles in exported_data.items():
            # Check existing group
            if group in self.custom_theme:
                for role, hex_color in roles.items():
                    # Parse color back to QColor
                    self.custom_theme[group][role] = QColor(hex_color)

        # Build new palette
        self._build_palette()

    # Import from *.qss
    def _import_from_qss(self, file_path) -> None:
        # Open file
        with open(file_path, "r") as theme:
            exported_data = theme.read()

        # Pattern
        pattern = r'qproperty-(active|inactive|disabled)-([\w-]+):\s*(#[a-fA-F0-9]{6});'

        # Find patterns
        matches = re.findall(pattern, exported_data)

        # Check matches
        if not matches:
            return

        # Browse groups, roles and colors in matches
        for group_raw, role, hex_color in matches:
            # Get group
            group = group_raw.capitalize()
            
            # Set it to custom theme
            self.custom_theme[group][role] = QColor(hex_color)

        # Build palette
        self._build_palette()

    # Import from *.py
    def _import_from_py(self, file_path) -> None:
        # Preparing dynamic imort
        file_path = Path(file_path)

        # Module name without type
        module_name = file_path.stem 

        # Create path for import
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        theme_module = importlib.util.module_from_spec(spec)
        
        # Run module
        spec.loader.exec_module(theme_module)

        # Check if module has THEME_DATA
        if hasattr(theme_module, "THEME_DATA"):
            # Load data
            data = theme_module.THEME_DATA
            
            # Load like from json
            for group_name, roles in data.items():
                # Normalize group 
                group = group_name.capitalize()

                # Role name and color
                for role_name, hex_color in roles.items():
                    self.custom_theme[group][role_name] = QColor(hex_color)

            # 4. Aplikace
            self._build_palette()

    # Export as *.json
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

        file_content = f"THEME_DATA = {export_data}"

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
                lines.append(f"    qproperty-{group_name}-{role}: {hex_val};")
        
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
            # Show error dialog
            ...
            print(e) 