# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'style_creator.ui'
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

class Ui_StyleCreator(object):
    def setupUi(self, StyleCreator):
        if not StyleCreator.objectName():
            StyleCreator.setObjectName(u"StyleCreator")
        StyleCreator.resize(400, 300)
        self.mainLayout = QVBoxLayout(StyleCreator)
        self.mainLayout.setSpacing(9)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(9, 9, 9, 9)
        self.exampleTextLabel = QLabel(StyleCreator)
        self.exampleTextLabel.setObjectName(u"exampleTextLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exampleTextLabel.sizePolicy().hasHeightForWidth())
        self.exampleTextLabel.setSizePolicy(sizePolicy)
        self.exampleTextLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.exampleTextLabel)

        self.foregroundButton = QPushButton(StyleCreator)
        self.foregroundButton.setObjectName(u"foregroundButton")
        self.foregroundButton.setCheckable(False)

        self.mainLayout.addWidget(self.foregroundButton)

        self.backgroundButton = QPushButton(StyleCreator)
        self.backgroundButton.setObjectName(u"backgroundButton")
        self.backgroundButton.setCheckable(False)

        self.mainLayout.addWidget(self.backgroundButton)

        self.boldButton = QPushButton(StyleCreator)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setCheckable(True)
        self.boldButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.boldButton)

        self.italicButton = QPushButton(StyleCreator)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setCheckable(True)
        self.italicButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.italicButton)

        self.underlineButton = QPushButton(StyleCreator)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setCheckable(True)
        self.underlineButton.setAutoDefault(False)

        self.mainLayout.addWidget(self.underlineButton)

        self.caseComboBox = QComboBox(StyleCreator)
        self.caseComboBox.addItem("")
        self.caseComboBox.addItem("")
        self.caseComboBox.setObjectName(u"caseComboBox")

        self.mainLayout.addWidget(self.caseComboBox)

        self.resetButton = QPushButton(StyleCreator)
        self.resetButton.setObjectName(u"resetButton")

        self.mainLayout.addWidget(self.resetButton)

        self.okButton = QPushButton(StyleCreator)
        self.okButton.setObjectName(u"okButton")

        self.mainLayout.addWidget(self.okButton)

        self.mainLayout.setStretch(0, 1)

        self.retranslateUi(StyleCreator)

        QMetaObject.connectSlotsByName(StyleCreator)
    # setupUi

    def retranslateUi(self, StyleCreator):
        StyleCreator.setWindowTitle(QCoreApplication.translate("StyleCreator", u"Dialog", None))
        self.exampleTextLabel.setText(QCoreApplication.translate("StyleCreator", u"example text", None))
        self.foregroundButton.setText(QCoreApplication.translate("StyleCreator", u"Foreground", None))
        self.backgroundButton.setText(QCoreApplication.translate("StyleCreator", u"Backgound", None))
        self.boldButton.setText(QCoreApplication.translate("StyleCreator", u"Bold", None))
        self.italicButton.setText(QCoreApplication.translate("StyleCreator", u"Italic", None))
        self.underlineButton.setText(QCoreApplication.translate("StyleCreator", u"Underline", None))
        self.caseComboBox.setItemText(0, QCoreApplication.translate("StyleCreator", u"abcdef", None))
        self.caseComboBox.setItemText(1, QCoreApplication.translate("StyleCreator", u"ABCDEF", None))

        self.resetButton.setText(QCoreApplication.translate("StyleCreator", u"Reset", None))
        self.okButton.setText(QCoreApplication.translate("StyleCreator", u"Ok", None))
    # retranslateUi

