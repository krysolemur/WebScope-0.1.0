# StyleCreator.py

from PySide6.QtWidgets import QDialog, QTreeWidgetItem # type: ignore
from PySide6.QtCore import Qt # type: ignore

from noctua.ui_gen.StyleCreator import Ui_StyleCreator

class StyleCreator(QDialog):

    # Constructor
    def __init__(self) -> None:

        # Init parents
        super().__init__()

        # All widgets
        self.all_widgets = {
            "Buttons": [
                "QPushButton", "QToolButton", "QRadioButton", "QCheckBox", "QCommandLinkButton"
            ],
            "Input Widgets": [
                "QLineEdit", "QTextEdit", "QPlainTextEdit", "QSpinBox", "QDoubleSpinBox",
                "QComboBox", "QFontComboBox", "QDateEdit", "QTimeEdit", "QDateTimeEdit", "QDial"
            ],
            "Display Widgets": [
                "QLabel", "QProgressBar", "QLCDNumber", "QStackedWidget", "QPixmap"
            ],
            "Containers": [
                "QGroupBox", "QScrollArea", "QFrame", "QTabWidget", "QToolBox", "QDockWidget"
            ],
            "Views & Tables": [
                "QListView", "QTreeView", "QTableView", "QColumnView", "QHeaderView", "QTabBar"
            ],
            "Navigation & Windows": [
                "QMainWindow", "QMenuBar", "QMenu", "QStatusBar", "QToolBar", "QSizeGrip"
            ]
        }

        # Load Ui
        self.ui = Ui_StyleCreator()

        # Setup Ui
        self.ui.setupUi(self)
        
        # Setup ui logic
        self._setup_ui_logic()
    
    # Setup ui logic
    def _setup_ui_logic(self):
        # Load item into tree
        self.load_widgets_into_tree(self.all_widgets)
        
        # Connect search
        self.ui.le_widget_search.textChanged.connect(self._filter_tree)
        
        # Double click to insert selector
        self.ui.tree_widgets.itemDoubleClicked.connect(self._on_item_double_clicked)

    # Load widgets into tree view
    def load_widgets_into_tree(self, data_dict):
        # Clear view
        self.ui.tree_widgets.clear()
        
        # Browse category and widgets
        for category, widgets in data_dict.items():
            # Create category
            parent_item = QTreeWidgetItem(self.ui.tree_widgets)
            parent_item.setText(0, category)
            parent_item.setFlags(parent_item.flags() & ~Qt.ItemIsSelectable)
            
            # Bold style for categories
            font = parent_item.font(0)
            font.setBold(True)
            parent_item.setFont(0, font)

            # All widgets
            for widget_name in sorted(widgets):
                # Child item for widget
                child_item = QTreeWidgetItem(parent_item)
                child_item.setText(0, widget_name)
            
            # Autmaticly expand categories
            parent_item.setExpanded(True)

    # Filter tree view by seatch
    def _filter_tree(self, text):
        # Browse categories
        for i in range(self.ui.tree_widgets.topLevelItemCount()):
            parent = self.ui.tree_widgets.topLevelItem(i)
            any_child_visible = False
            
            # Browse widgets in categories
            for j in range(parent.childCount()):
                child = parent.child(j)
                should_show = text.lower() in child.text(0).lower()
                child.setHidden(not should_show)
                if should_show:
                    any_child_visible = True
            
            # Show categort if there is no visible widget
            parent.setHidden(not any_child_visible and text != "")

    # Set double click action
    def _on_item_double_clicked(self, item, column):
        # Check if its not category
        if item.childCount() == 0:
            name = item.text(0)
            template = f"{name} {{\n    \n}}\n"
            self.ui.txt_css_editor.insertPlainText(template)
            self.ui.txt_css_editor.setFocus()

