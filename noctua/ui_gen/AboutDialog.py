# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutDialog.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        if not aboutDialog.objectName():
            aboutDialog.setObjectName(u"aboutDialog")
        aboutDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(aboutDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.versionLayout = QHBoxLayout()
        self.versionLayout.setObjectName(u"versionLayout")
        self.versionLayout.setContentsMargins(6, 6, 6, 6)
        self.versionLabel = QLabel(aboutDialog)
        self.versionLabel.setObjectName(u"versionLabel")

        self.versionLayout.addWidget(self.versionLabel)


        self.mainLayout.addLayout(self.versionLayout)


        self.retranslateUi(aboutDialog)

        QMetaObject.connectSlotsByName(aboutDialog)
    # setupUi

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QCoreApplication.translate("aboutDialog", u"Dialog", None))
        self.versionLabel.setText(QCoreApplication.translate("aboutDialog", u"Version: ", None))
    # retranslateUi

