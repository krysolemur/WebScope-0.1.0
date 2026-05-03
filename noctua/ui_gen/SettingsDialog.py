# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setWindowModality(Qt.NonModal)
        SettingsDialog.resize(910, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setMinimumSize(QSize(0, 0))
        SettingsDialog.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        SettingsDialog.setContextMenuPolicy(Qt.NoContextMenu)
        SettingsDialog.setSizeGripEnabled(False)
        SettingsDialog.setModal(True)
        self.mainLayout = QVBoxLayout(SettingsDialog)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsLayout = QHBoxLayout()
        self.settingsLayout.setSpacing(0)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.settingsView = QListWidget(SettingsDialog)
        QListWidgetItem(self.settingsView)
        QListWidgetItem(self.settingsView)
        QListWidgetItem(self.settingsView)
        self.settingsView.setObjectName(u"settingsView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settingsView.sizePolicy().hasHeightForWidth())
        self.settingsView.setSizePolicy(sizePolicy1)

        self.settingsLayout.addWidget(self.settingsView)

        self.settingsWidget = QStackedWidget(SettingsDialog)
        self.settingsWidget.setObjectName(u"settingsWidget")
        sizePolicy.setHeightForWidth(self.settingsWidget.sizePolicy().hasHeightForWidth())
        self.settingsWidget.setSizePolicy(sizePolicy)
        self.settingsWidget.setMinimumSize(QSize(0, 0))
        self.settingsWidget.setFrameShape(QFrame.NoFrame)
        self.settingsWidget.setFrameShadow(QFrame.Sunken)

        self.settingsLayout.addWidget(self.settingsWidget)


        self.mainLayout.addLayout(self.settingsLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.buttonsLayout.setContentsMargins(6, 6, 6, 6)
        self.cancelButton = QPushButton(SettingsDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy2)

        self.buttonsLayout.addWidget(self.cancelButton)

        self.resetButton = QPushButton(SettingsDialog)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy2.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy2)

        self.buttonsLayout.addWidget(self.resetButton)

        self.applyButton = QPushButton(SettingsDialog)
        self.applyButton.setObjectName(u"applyButton")
        sizePolicy2.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy2)

        self.buttonsLayout.addWidget(self.applyButton)


        self.mainLayout.addLayout(self.buttonsLayout)

        self.statusLayout = QHBoxLayout()
        self.statusLayout.setSpacing(3)
        self.statusLayout.setObjectName(u"statusLayout")
        self.statusLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.statusLayout.setContentsMargins(3, 3, 3, 3)
        self.statusLabel = QLabel(SettingsDialog)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setFrameShape(QFrame.NoFrame)

        self.statusLayout.addWidget(self.statusLabel)


        self.mainLayout.addLayout(self.statusLayout)

        self.mainLayout.setStretch(0, 1)

        self.retranslateUi(SettingsDialog)

        self.settingsView.setCurrentRow(0)
        self.settingsWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))

        __sortingEnabled = self.settingsView.isSortingEnabled()
        self.settingsView.setSortingEnabled(False)
        ___qlistwidgetitem = self.settingsView.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"General", None))
        ___qlistwidgetitem1 = self.settingsView.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("SettingsDialog", u"Logging", None))
        ___qlistwidgetitem2 = self.settingsView.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("SettingsDialog", u"Source code ", None))
        self.settingsView.setSortingEnabled(__sortingEnabled)

        self.cancelButton.setText(QCoreApplication.translate("SettingsDialog", u"Close", None))
        self.resetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.applyButton.setText(QCoreApplication.translate("SettingsDialog", u"Apply", None))
        self.statusLabel.setText(QCoreApplication.translate("SettingsDialog", u"Status: ", None))
    # retranslateUi

