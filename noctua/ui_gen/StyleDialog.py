# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StyleDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_styleDialog(object):
    def setupUi(self, styleDialog):
        if not styleDialog.objectName():
            styleDialog.setObjectName(u"styleDialog")
        styleDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(styleDialog)
        self.mainLayout.setSpacing(9)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(9, 9, 9, 9)
        self.exampleTextLabel = QLabel(styleDialog)
        self.exampleTextLabel.setObjectName(u"exampleTextLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exampleTextLabel.sizePolicy().hasHeightForWidth())
        self.exampleTextLabel.setSizePolicy(sizePolicy)
        self.exampleTextLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.exampleTextLabel)

        self.foregroundButton = QPushButton(styleDialog)
        self.foregroundButton.setObjectName(u"foregroundButton")
        self.foregroundButton.setCheckable(False)

        self.mainLayout.addWidget(self.foregroundButton)

        self.backgroundButton = QPushButton(styleDialog)
        self.backgroundButton.setObjectName(u"backgroundButton")
        self.backgroundButton.setCheckable(False)

        self.mainLayout.addWidget(self.backgroundButton)

        self.boldButton = QPushButton(styleDialog)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setCheckable(True)
        self.boldButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.boldButton)

        self.italicButton = QPushButton(styleDialog)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setCheckable(True)
        self.italicButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.italicButton)

        self.underlineButton = QPushButton(styleDialog)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setCheckable(True)
        self.underlineButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.underlineButton)

        self.caseComboBox = QComboBox(styleDialog)
        self.caseComboBox.addItem("")
        self.caseComboBox.addItem("")
        self.caseComboBox.setObjectName(u"caseComboBox")

        self.mainLayout.addWidget(self.caseComboBox)

        self.resetButton = QPushButton(styleDialog)
        self.resetButton.setObjectName(u"resetButton")

        self.mainLayout.addWidget(self.resetButton)

        self.okButton = QPushButton(styleDialog)
        self.okButton.setObjectName(u"okButton")

        self.mainLayout.addWidget(self.okButton)

        self.mainLayout.setStretch(0, 1)

        self.retranslateUi(styleDialog)

        QMetaObject.connectSlotsByName(styleDialog)
    # setupUi

    def retranslateUi(self, styleDialog):
        styleDialog.setWindowTitle(QCoreApplication.translate("styleDialog", u"Dialog", None))
        self.exampleTextLabel.setText(QCoreApplication.translate("styleDialog", u"example text", None))
        self.foregroundButton.setText(QCoreApplication.translate("styleDialog", u"Foreground", None))
        self.backgroundButton.setText(QCoreApplication.translate("styleDialog", u"Backgound", None))
        self.boldButton.setText(QCoreApplication.translate("styleDialog", u"Bold", None))
        self.italicButton.setText(QCoreApplication.translate("styleDialog", u"Italic", None))
        self.underlineButton.setText(QCoreApplication.translate("styleDialog", u"Underline", None))
        self.caseComboBox.setItemText(0, QCoreApplication.translate("styleDialog", u"abcdef", None))
        self.caseComboBox.setItemText(1, QCoreApplication.translate("styleDialog", u"ABCDEF", None))

        self.resetButton.setText(QCoreApplication.translate("styleDialog", u"Reset", None))
        self.okButton.setText(QCoreApplication.translate("styleDialog", u"Ok", None))
    # retranslateUi

