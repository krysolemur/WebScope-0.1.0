# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ErrorDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        if not ErrorDialog.objectName():
            ErrorDialog.setObjectName(u"ErrorDialog")
        ErrorDialog.resize(480, 350)
        self.lyt_main = QVBoxLayout(ErrorDialog)
        self.lyt_main.setSpacing(3)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_main.setContentsMargins(3, 3, 3, 3)
        self.lyt_header = QHBoxLayout()
        self.lyt_header.setSpacing(6)
        self.lyt_header.setObjectName(u"lyt_header")
        self.lbl_icon = QLabel(ErrorDialog)
        self.lbl_icon.setObjectName(u"lbl_icon")
        self.lbl_icon.setMinimumSize(QSize(32, 32))
        self.lbl_icon.setMaximumSize(QSize(32, 32))

        self.lyt_header.addWidget(self.lbl_icon)

        self.lbl_title = QLabel(ErrorDialog)
        self.lbl_title.setObjectName(u"lbl_title")

        self.lyt_header.addWidget(self.lbl_title)


        self.lyt_main.addLayout(self.lyt_header)

        self.lyt_toggle = QHBoxLayout()
        self.lyt_toggle.setObjectName(u"lyt_toggle")
        self.btn_details_toggle = QPushButton(ErrorDialog)
        self.btn_details_toggle.setObjectName(u"btn_details_toggle")
        self.btn_details_toggle.setCheckable(True)
        self.btn_details_toggle.setFlat(True)

        self.lyt_toggle.addWidget(self.btn_details_toggle)

        self.spc_toggle_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lyt_toggle.addItem(self.spc_toggle_spacer)


        self.lyt_main.addLayout(self.lyt_toggle)

        self.te_error_details = QTextEdit(ErrorDialog)
        self.te_error_details.setObjectName(u"te_error_details")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.te_error_details.sizePolicy().hasHeightForWidth())
        self.te_error_details.setSizePolicy(sizePolicy)
        self.te_error_details.setVisible(False)
        self.te_error_details.setLineWrapMode(QTextEdit.NoWrap)
        self.te_error_details.setReadOnly(True)

        self.lyt_main.addWidget(self.te_error_details)

        self.lyt_buttons = QHBoxLayout()
        self.lyt_buttons.setObjectName(u"lyt_buttons")
        self.btn_copy = QPushButton(ErrorDialog)
        self.btn_copy.setObjectName(u"btn_copy")

        self.lyt_buttons.addWidget(self.btn_copy)

        self.spc_button_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lyt_buttons.addItem(self.spc_button_spacer)

        self.btn_close = QPushButton(ErrorDialog)
        self.btn_close.setObjectName(u"btn_close")

        self.lyt_buttons.addWidget(self.btn_close)


        self.lyt_main.addLayout(self.lyt_buttons)


        self.retranslateUi(ErrorDialog)

        QMetaObject.connectSlotsByName(ErrorDialog)
    # setupUi

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(QCoreApplication.translate("ErrorDialog", u"Error", None))
        self.lbl_title.setText("")
        self.btn_details_toggle.setText(QCoreApplication.translate("ErrorDialog", u"\u25b6 Show Details", None))
        self.btn_copy.setText(QCoreApplication.translate("ErrorDialog", u"Copy", None))
        self.btn_close.setText(QCoreApplication.translate("ErrorDialog", u"Close", None))
    # retranslateUi

