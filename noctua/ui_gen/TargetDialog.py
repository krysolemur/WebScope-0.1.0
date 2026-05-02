# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TargetDialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TargetDialog(object):
    def setupUi(self, TargetDialog):
        if not TargetDialog.objectName():
            TargetDialog.setObjectName(u"TargetDialog")
        TargetDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(TargetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setTargetLayout = QHBoxLayout()
        self.setTargetLayout.setObjectName(u"setTargetLayout")
        self.setTargetLayout.setContentsMargins(6, 6, 6, 6)
        self.setTargetLabel = QLabel(TargetDialog)
        self.setTargetLabel.setObjectName(u"setTargetLabel")

        self.setTargetLayout.addWidget(self.setTargetLabel)

        self.setTargetLineEdit = QLineEdit(TargetDialog)
        self.setTargetLineEdit.setObjectName(u"setTargetLineEdit")

        self.setTargetLayout.addWidget(self.setTargetLineEdit)

        self.setTargetLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.setTargetLayout)

        self.setTargetButton = QPushButton(TargetDialog)
        self.setTargetButton.setObjectName(u"setTargetButton")

        self.verticalLayout.addWidget(self.setTargetButton)


        self.retranslateUi(TargetDialog)

        QMetaObject.connectSlotsByName(TargetDialog)
    # setupUi

    def retranslateUi(self, TargetDialog):
        TargetDialog.setWindowTitle(QCoreApplication.translate("TargetDialog", u"Dialog", None))
        self.setTargetLabel.setText(QCoreApplication.translate("TargetDialog", u"Web URL: ", None))
        self.setTargetLineEdit.setPlaceholderText(QCoreApplication.translate("TargetDialog", u"https://example.url", None))
        self.setTargetButton.setText(QCoreApplication.translate("TargetDialog", u"Set target", None))
    # retranslateUi

