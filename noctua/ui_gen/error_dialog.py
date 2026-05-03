# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_dialog.ui'
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
        ErrorDialog.resize(400, 250)
        self.lyt_main = QVBoxLayout(ErrorDialog)
        self.lyt_main.setSpacing(15)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_header = QHBoxLayout()
        self.lyt_header.setSpacing(10)
        self.lyt_header.setObjectName(u"lyt_header")
        self.lbl_icon = QLabel(ErrorDialog)
        self.lbl_icon.setObjectName(u"lbl_icon")
        self.lbl_icon.setMaximumSize(QSize(32, 32))
        self.lbl_icon.setScaledContents(True)

        self.lyt_header.addWidget(self.lbl_icon)

        self.lbl_title = QLabel(ErrorDialog)
        self.lbl_title.setObjectName(u"lbl_title")

        self.lyt_header.addWidget(self.lbl_title)


        self.lyt_main.addLayout(self.lyt_header)

        self.lyt_content = QVBoxLayout()
        self.lyt_content.setSpacing(8)
        self.lyt_content.setObjectName(u"lyt_content")
        self.lbl_error_message = QLabel(ErrorDialog)
        self.lbl_error_message.setObjectName(u"lbl_error_message")
        self.lbl_error_message.setWordWrap(True)

        self.lyt_content.addWidget(self.lbl_error_message)

        self.te_error_details = QTextEdit(ErrorDialog)
        self.te_error_details.setObjectName(u"te_error_details")
        self.te_error_details.setReadOnly(True)

        self.lyt_content.addWidget(self.te_error_details)

        self.lyt_buttons = QHBoxLayout()
        self.lyt_buttons.setObjectName(u"lyt_buttons")
        self.spc_button_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lyt_buttons.addItem(self.spc_button_spacer)

        self.btn_copy = QPushButton(ErrorDialog)
        self.btn_copy.setObjectName(u"btn_copy")

        self.lyt_buttons.addWidget(self.btn_copy)

        self.btn_close = QPushButton(ErrorDialog)
        self.btn_close.setObjectName(u"btn_close")

        self.lyt_buttons.addWidget(self.btn_close)


        self.lyt_content.addLayout(self.lyt_buttons)


        self.lyt_main.addLayout(self.lyt_content)


        self.retranslateUi(ErrorDialog)

        QMetaObject.connectSlotsByName(ErrorDialog)
    # setupUi

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(QCoreApplication.translate("ErrorDialog", u"Error", None))
        self.lbl_icon.setText("")
        self.lbl_title.setText(QCoreApplication.translate("ErrorDialog", u"System Message", None))
        self.lbl_error_message.setText(QCoreApplication.translate("ErrorDialog", u"An error has occurred in the application.", None))
        self.btn_copy.setText(QCoreApplication.translate("ErrorDialog", u"Copy", None))
        self.btn_close.setText(QCoreApplication.translate("ErrorDialog", u"Close", None))
    # retranslateUi

