# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThemeCreator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ThemeCreator(object):
    def setupUi(self, ThemeCreator):
        if not ThemeCreator.objectName():
            ThemeCreator.setObjectName(u"ThemeCreator")
        ThemeCreator.resize(900, 750)
        self.lay_main = QVBoxLayout(ThemeCreator)
        self.lay_main.setSpacing(15)
        self.lay_main.setContentsMargins(15, 15, 15, 15)
        self.lay_main.setObjectName(u"lay_main")
        self.grp_state = QGroupBox(ThemeCreator)
        self.grp_state.setObjectName(u"grp_state")
        self.lay_state = QHBoxLayout(self.grp_state)
        self.lay_state.setObjectName(u"lay_state")
        self.cb_state = QComboBox(self.grp_state)
        self.cb_state.addItem("")
        self.cb_state.addItem("")
        self.cb_state.addItem("")
        self.cb_state.setObjectName(u"cb_state")

        self.lay_state.addWidget(self.cb_state)

        self.h_sp_state = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lay_state.addItem(self.h_sp_state)


        self.lay_main.addWidget(self.grp_state)

        self.tw_palette_roles = QTreeWidget(ThemeCreator)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        QTreeWidgetItem(self.tw_palette_roles)
        self.tw_palette_roles.setObjectName(u"tw_palette_roles")
        self.tw_palette_roles.setAlternatingRowColors(True)
        self.tw_palette_roles.setAnimated(True)
        self.tw_palette_roles.header().setDefaultSectionSize(200)
        self.tw_palette_roles.header().setStretchLastSection(True)

        self.lay_main.addWidget(self.tw_palette_roles)

        self.lay_buttons = QHBoxLayout()
        self.lay_buttons.setObjectName(u"lay_buttons")
        self.btn_set_color = QPushButton(ThemeCreator)
        self.btn_set_color.setObjectName(u"btn_set_color")
        self.btn_set_color.setMinimumSize(QSize(0, 40))

        self.lay_buttons.addWidget(self.btn_set_color)

        self.btn_reset = QPushButton(ThemeCreator)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(0, 40))

        self.lay_buttons.addWidget(self.btn_reset)

        self.btn_full_preview = QPushButton(ThemeCreator)
        self.btn_full_preview.setObjectName(u"btn_full_preview")
        self.btn_full_preview.setMinimumSize(QSize(0, 40))

        self.lay_buttons.addWidget(self.btn_full_preview)


        self.lay_main.addLayout(self.lay_buttons)

        self.grp_io = QGroupBox(ThemeCreator)
        self.grp_io.setObjectName(u"grp_io")
        self.grid_io = QGridLayout(self.grp_io)
        self.grid_io.setObjectName(u"grid_io")
        self.l_target_format = QLabel(self.grp_io)
        self.l_target_format.setObjectName(u"l_target_format")

        self.grid_io.addWidget(self.l_target_format, 0, 0, 1, 1)

        self.cb_format = QComboBox(self.grp_io)
        self.cb_format.addItem("")
        self.cb_format.addItem("")
        self.cb_format.addItem("")
        self.cb_format.setObjectName(u"cb_format")

        self.grid_io.addWidget(self.cb_format, 0, 1, 1, 1)

        self.lay_io_actions = QHBoxLayout()
        self.lay_io_actions.setObjectName(u"lay_io_actions")
        self.btn_import = QPushButton(self.grp_io)
        self.btn_import.setObjectName(u"btn_import")

        self.lay_io_actions.addWidget(self.btn_import)

        self.btn_export = QPushButton(self.grp_io)
        self.btn_export.setObjectName(u"btn_export")

        self.lay_io_actions.addWidget(self.btn_export)


        self.grid_io.addLayout(self.lay_io_actions, 1, 0, 1, 2)


        self.lay_main.addWidget(self.grp_io)


        self.retranslateUi(ThemeCreator)

        QMetaObject.connectSlotsByName(ThemeCreator)
    # setupUi

    def retranslateUi(self, ThemeCreator):
        ThemeCreator.setWindowTitle(QCoreApplication.translate("ThemeCreator", u"Ultimate Qt Palette Designer", None))
        self.grp_state.setTitle(QCoreApplication.translate("ThemeCreator", u"Select Color Group (State)", None))
        self.cb_state.setItemText(0, QCoreApplication.translate("ThemeCreator", u"Active (Normal)", None))
        self.cb_state.setItemText(1, QCoreApplication.translate("ThemeCreator", u"Inactive (Window in background)", None))
        self.cb_state.setItemText(2, QCoreApplication.translate("ThemeCreator", u"Disabled (Grayed out)", None))

        ___qtreewidgetitem = self.tw_palette_roles.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("ThemeCreator", u"Visual Preview", None))
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ThemeCreator", u"Hex Value", None))
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ThemeCreator", u"Color Role", None))

        __sortingEnabled = self.tw_palette_roles.isSortingEnabled()
        self.tw_palette_roles.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tw_palette_roles.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("ThemeCreator", u"Window", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem1.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"General background color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem2 = self.tw_palette_roles.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("ThemeCreator", u"WindowText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem2.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"General foreground color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem3 = self.tw_palette_roles.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("ThemeCreator", u"Base", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem3.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Used as the background color for text entry widgets.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem4 = self.tw_palette_roles.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("ThemeCreator", u"AlternateBase", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem4.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Used as the alternate background color in views with alternating row colors.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem5 = self.tw_palette_roles.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("ThemeCreator", u"Text", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem5.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"The foreground color used with Base.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem6 = self.tw_palette_roles.topLevelItem(5)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("ThemeCreator", u"Button", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem6.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"The general button background color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem7 = self.tw_palette_roles.topLevelItem(6)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("ThemeCreator", u"ButtonText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem7.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A foreground color used with the Button color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem8 = self.tw_palette_roles.topLevelItem(7)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("ThemeCreator", u"BrightText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem8.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A text color that is very different from WindowText (e.g. for dark backgrounds).", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem9 = self.tw_palette_roles.topLevelItem(8)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("ThemeCreator", u"Light", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem9.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Lighter than Button color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem10 = self.tw_palette_roles.topLevelItem(9)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("ThemeCreator", u"Midlight", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem10.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Between Button and Light.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem11 = self.tw_palette_roles.topLevelItem(10)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("ThemeCreator", u"Dark", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem11.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Darker than Button color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem12 = self.tw_palette_roles.topLevelItem(11)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("ThemeCreator", u"Mid", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem12.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Between Button and Dark.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem13 = self.tw_palette_roles.topLevelItem(12)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("ThemeCreator", u"Shadow", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem13.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A very dark color.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem14 = self.tw_palette_roles.topLevelItem(13)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("ThemeCreator", u"Highlight", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem14.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A color to indicate a selected or focused item.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem15 = self.tw_palette_roles.topLevelItem(14)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("ThemeCreator", u"HighlightedText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem15.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A text color that contrasts with Highlight.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem16 = self.tw_palette_roles.topLevelItem(15)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("ThemeCreator", u"Link", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem16.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A text color used for unvisited hyperlinks.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem17 = self.tw_palette_roles.topLevelItem(16)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("ThemeCreator", u"LinkVisited", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem17.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"A text color used for already visited hyperlinks.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem18 = self.tw_palette_roles.topLevelItem(17)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("ThemeCreator", u"PlaceholderText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem18.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Used for input placeholder text.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem19 = self.tw_palette_roles.topLevelItem(18)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("ThemeCreator", u"ToolTipBase", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem19.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Used as the background color for QToolTip.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem20 = self.tw_palette_roles.topLevelItem(19)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("ThemeCreator", u"ToolTipText", None))
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem20.setToolTip(0, QCoreApplication.translate("ThemeCreator", u"Used as the foreground color for QToolTip.", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem21 = self.tw_palette_roles.topLevelItem(20)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("ThemeCreator", u"NoRole", None))
        self.tw_palette_roles.setSortingEnabled(__sortingEnabled)

        self.btn_set_color.setText(QCoreApplication.translate("ThemeCreator", u"Set Selected Role Color...", None))
        self.btn_reset.setText(QCoreApplication.translate("ThemeCreator", u"Reset Role", None))
        self.btn_full_preview.setText(QCoreApplication.translate("ThemeCreator", u"Show Full Live Preview", None))
        self.grp_io.setTitle(QCoreApplication.translate("ThemeCreator", u"Import / Export", None))
        self.l_target_format.setText(QCoreApplication.translate("ThemeCreator", u"Target Format:", None))
        self.cb_format.setItemText(0, QCoreApplication.translate("ThemeCreator", u"JSON File (*.json)", None))
        self.cb_format.setItemText(1, QCoreApplication.translate("ThemeCreator", u"Qt Stylesheet (*.qss)", None))
        self.cb_format.setItemText(2, QCoreApplication.translate("ThemeCreator", u"Python Dict (*.py)", None))

        self.btn_import.setText(QCoreApplication.translate("ThemeCreator", u"Import Theme", None))
        self.btn_export.setText(QCoreApplication.translate("ThemeCreator", u"Export Theme", None))
    # retranslateUi

