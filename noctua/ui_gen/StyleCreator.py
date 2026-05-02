# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StyleCreator.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
class Ui_StyleCreator(object):
    def setupUi(self, StyleCreator):
        if not StyleCreator.objectName():
            StyleCreator.setObjectName(u"StyleCreator")
        StyleCreator.resize(800, 600)
        self.lyt_main = QVBoxLayout(StyleCreator)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_content = QHBoxLayout()
        self.lyt_content.setObjectName(u"lyt_content")
        self.lyt_left_panel = QVBoxLayout()
        self.lyt_left_panel.setObjectName(u"lyt_left_panel")
        self.lbl_widgets = QLabel(StyleCreator)
        self.lbl_widgets.setObjectName(u"lbl_widgets")
        font = QFont()
        font.setBold(True)
        self.lbl_widgets.setFont(font)

        self.lyt_left_panel.addWidget(self.lbl_widgets)

        self.le_widget_search = QLineEdit(StyleCreator)
        self.le_widget_search.setObjectName(u"le_widget_search")

        self.lyt_left_panel.addWidget(self.le_widget_search)

        self.tree_widgets = QTreeWidget(StyleCreator)
        self.tree_widgets.setObjectName(u"tree_widgets")
        self.tree_widgets.header().setVisible(False)

        self.lyt_left_panel.addWidget(self.tree_widgets)


        self.lyt_content.addLayout(self.lyt_left_panel)

        self.lyt_right_panel = QVBoxLayout()
        self.lyt_right_panel.setObjectName(u"lyt_right_panel")
        self.lbl_editor = QLabel(StyleCreator)
        self.lbl_editor.setObjectName(u"lbl_editor")
        self.lbl_editor.setFont(font)

        self.lyt_right_panel.addWidget(self.lbl_editor)

        self.txt_css_editor = QPlainTextEdit(StyleCreator)
        self.txt_css_editor.setObjectName(u"txt_css_editor")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        self.txt_css_editor.setFont(font1)

        self.lyt_right_panel.addWidget(self.txt_css_editor)


        self.lyt_content.addLayout(self.lyt_right_panel)

        self.lyt_content.setStretch(0, 1)
        self.lyt_content.setStretch(1, 2)

        self.lyt_main.addLayout(self.lyt_content)

        self.lyt_footer = QHBoxLayout()
        self.lyt_footer.setObjectName(u"lyt_footer")
        self.btn_live_preview = QPushButton(StyleCreator)
        self.btn_live_preview.setObjectName(u"btn_live_preview")

        self.lyt_footer.addWidget(self.btn_live_preview)

        self.spc_footer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lyt_footer.addItem(self.spc_footer)

        self.btn_cancel = QPushButton(StyleCreator)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.lyt_footer.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(StyleCreator)
        self.btn_save.setObjectName(u"btn_save")

        self.lyt_footer.addWidget(self.btn_save)


        self.lyt_main.addLayout(self.lyt_footer)


        self.retranslateUi(StyleCreator)

        QMetaObject.connectSlotsByName(StyleCreator)
    # setupUi

    def retranslateUi(self, StyleCreator):
        StyleCreator.setWindowTitle(QCoreApplication.translate("StyleCreator", u"XyraEngine - Style Creator", None))
        self.lbl_widgets.setText(QCoreApplication.translate("StyleCreator", u"Widget Hierarchy", None))
        self.le_widget_search.setPlaceholderText(QCoreApplication.translate("StyleCreator", u"Filter widgets...", None))
        ___qtreewidgetitem = self.tree_widgets.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("StyleCreator", u"Widget", None))
        self.lbl_editor.setText(QCoreApplication.translate("StyleCreator", u"QSS Editor", None))
        self.btn_live_preview.setText(QCoreApplication.translate("StyleCreator", u"Open Live Preview", None))
        self.btn_cancel.setText(QCoreApplication.translate("StyleCreator", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("StyleCreator", u"Save Stylesheet", None))
    # retranslateUi

