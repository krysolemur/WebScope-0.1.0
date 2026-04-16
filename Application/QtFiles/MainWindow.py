# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QTabWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(871, 600)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionRestart = QAction(MainWindow)
        self.actionRestart.setObjectName(u"actionRestart")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionSetTarget = QAction(MainWindow)
        self.actionSetTarget.setObjectName(u"actionSetTarget")
        self.actionDownloadSourceCode = QAction(MainWindow)
        self.actionDownloadSourceCode.setObjectName(u"actionDownloadSourceCode")
        self.actionXSS = QAction(MainWindow)
        self.actionXSS.setObjectName(u"actionXSS")
        self.actionSQLInjection = QAction(MainWindow)
        self.actionSQLInjection.setObjectName(u"actionSQLInjection")
        self.actionPlugins = QAction(MainWindow)
        self.actionPlugins.setObjectName(u"actionPlugins")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionInstall = QAction(MainWindow)
        self.actionInstall.setObjectName(u"actionInstall")
        self.actionReportBug = QAction(MainWindow)
        self.actionReportBug.setObjectName(u"actionReportBug")
        self.actionIdeas = QAction(MainWindow)
        self.actionIdeas.setObjectName(u"actionIdeas")
        self.actionManageUsers = QAction(MainWindow)
        self.actionManageUsers.setObjectName(u"actionManageUsers")
        self.actionInstall_own = QAction(MainWindow)
        self.actionInstall_own.setObjectName(u"actionInstall_own")
        self.actionThemeCreator = QAction(MainWindow)
        self.actionThemeCreator.setObjectName(u"actionThemeCreator")
        self.actionStylesheetCreator = QAction(MainWindow)
        self.actionStylesheetCreator.setObjectName(u"actionStylesheetCreator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QGridLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.toolsTabWidget = QTabWidget(self.centralwidget)
        self.toolsTabWidget.setObjectName(u"toolsTabWidget")
        self.sourceTab = QWidget()
        self.sourceTab.setObjectName(u"sourceTab")
        self.sourceLayout = QGridLayout(self.sourceTab)
        self.sourceLayout.setObjectName(u"sourceLayout")
        self.sourceLayout.setContentsMargins(0, 0, 0, 0)
        self.sourceTextEdit = QTextEdit(self.sourceTab)
        self.sourceTextEdit.setObjectName(u"sourceTextEdit")
        self.sourceTextEdit.setFrameShape(QFrame.NoFrame)
        self.sourceTextEdit.setFrameShadow(QFrame.Plain)
        self.sourceTextEdit.setReadOnly(True)

        self.sourceLayout.addWidget(self.sourceTextEdit, 0, 0, 1, 1)

        self.toolsTabWidget.addTab(self.sourceTab, "")
        self.networkTab = QWidget()
        self.networkTab.setObjectName(u"networkTab")
        self.toolsTabWidget.addTab(self.networkTab, "")
        self.consoleTab = QWidget()
        self.consoleTab.setObjectName(u"consoleTab")
        self.toolsTabWidget.addTab(self.consoleTab, "")

        self.mainLayout.addWidget(self.toolsTabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 871, 20))
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuTarget = QMenu(self.menubar)
        self.menuTarget.setObjectName(u"menuTarget")
        self.menuAttack = QMenu(self.menubar)
        self.menuAttack.setObjectName(u"menuAttack")
        self.menuInjections = QMenu(self.menuAttack)
        self.menuInjections.setObjectName(u"menuInjections")
        self.menuPlugins = QMenu(self.menubar)
        self.menuPlugins.setObjectName(u"menuPlugins")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuTarget.menuAction())
        self.menubar.addAction(self.menuAttack.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionSettings)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAbout)
        self.menuWindow.addAction(self.actionDocumentation)
        self.menuWindow.addAction(self.actionHelp)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionReportBug)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionRestart)
        self.menuWindow.addAction(self.actionQuit)
        self.menuTarget.addAction(self.actionSetTarget)
        self.menuTarget.addAction(self.actionDownloadSourceCode)
        self.menuAttack.addAction(self.menuInjections.menuAction())
        self.menuAttack.addAction(self.actionXSS)
        self.menuInjections.addAction(self.actionSQLInjection)
        self.menuPlugins.addAction(self.actionAdd)
        self.menuPlugins.addAction(self.actionInstall)
        self.menuTools.addAction(self.actionThemeCreator)
        self.menuTools.addAction(self.actionStylesheetCreator)

        self.retranslateUi(MainWindow)

        self.toolsTabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionRestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionSetTarget.setText(QCoreApplication.translate("MainWindow", u"Set target", None))
        self.actionDownloadSourceCode.setText(QCoreApplication.translate("MainWindow", u"Download source code", None))
        self.actionXSS.setText(QCoreApplication.translate("MainWindow", u"XSS", None))
        self.actionSQLInjection.setText(QCoreApplication.translate("MainWindow", u"SQL Injection", None))
        self.actionPlugins.setText(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.actionInstall.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionReportBug.setText(QCoreApplication.translate("MainWindow", u"Report bug", None))
        self.actionIdeas.setText(QCoreApplication.translate("MainWindow", u"Ideas", None))
        self.actionManageUsers.setText(QCoreApplication.translate("MainWindow", u"Manage users", None))
        self.actionInstall_own.setText(QCoreApplication.translate("MainWindow", u"Install own", None))
        self.actionThemeCreator.setText(QCoreApplication.translate("MainWindow", u"Theme creator", None))
        self.actionStylesheetCreator.setText(QCoreApplication.translate("MainWindow", u"Stylesheet creator", None))
        self.sourceTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolsTabWidget.setTabText(self.toolsTabWidget.indexOf(self.sourceTab), QCoreApplication.translate("MainWindow", u"Source", None))
        self.toolsTabWidget.setTabText(self.toolsTabWidget.indexOf(self.networkTab), QCoreApplication.translate("MainWindow", u"Network", None))
        self.toolsTabWidget.setTabText(self.toolsTabWidget.indexOf(self.consoleTab), QCoreApplication.translate("MainWindow", u"Console", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuTarget.setTitle(QCoreApplication.translate("MainWindow", u"Target", None))
        self.menuAttack.setTitle(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.menuInjections.setTitle(QCoreApplication.translate("MainWindow", u"Injections", None))
        self.menuPlugins.setTitle(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

