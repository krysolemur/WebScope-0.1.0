# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoggingPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_LoggingPage(object):
    def setupUi(self, LoggingPage):
        if not LoggingPage.objectName():
            LoggingPage.setObjectName(u"LoggingPage")
        LoggingPage.resize(967, 532)
        self.lyt_main = QVBoxLayout(LoggingPage)
        self.lyt_main.setSpacing(3)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_main.setContentsMargins(3, 3, 3, 3)
        self.sa_logger = QScrollArea(LoggingPage)
        self.sa_logger.setObjectName(u"sa_logger")
        self.sa_logger.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_logger.setWidgetResizable(True)
        self.sa_content = QWidget()
        self.sa_content.setObjectName(u"sa_content")
        self.sa_content.setGeometry(QRect(0, 0, 959, 524))
        self.lyt_scroll = QVBoxLayout(self.sa_content)
        self.lyt_scroll.setObjectName(u"lyt_scroll")
        self.lyt_console_section = QVBoxLayout()
        self.lyt_console_section.setObjectName(u"lyt_console_section")
        self.lbl_console_header = QLabel(self.sa_content)
        self.lbl_console_header.setObjectName(u"lbl_console_header")
        font = QFont()
        font.setBold(True)
        self.lbl_console_header.setFont(font)
        self.lbl_console_header.setMargin(0)

        self.lyt_console_section.addWidget(self.lbl_console_header)

        self.lyt_console_time = QHBoxLayout()
        self.lyt_console_time.setObjectName(u"lyt_console_time")
        self.lbl_console_time = QLabel(self.sa_content)
        self.lbl_console_time.setObjectName(u"lbl_console_time")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_console_time.sizePolicy().hasHeightForWidth())
        self.lbl_console_time.setSizePolicy(sizePolicy)

        self.lyt_console_time.addWidget(self.lbl_console_time)

        self.cb_console_time = QComboBox(self.sa_content)
        self.cb_console_time.addItem("")
        self.cb_console_time.addItem("")
        self.cb_console_time.setObjectName(u"cb_console_time")

        self.lyt_console_time.addWidget(self.cb_console_time)


        self.lyt_console_section.addLayout(self.lyt_console_time)

        self.lyt_console_buttons = QGridLayout()
        self.lyt_console_buttons.setObjectName(u"lyt_console_buttons")
        self.btn_console_info = QPushButton(self.sa_content)
        self.btn_console_info.setObjectName(u"btn_console_info")
        self.btn_console_info.setCheckable(True)

        self.lyt_console_buttons.addWidget(self.btn_console_info, 0, 0, 1, 1)

        self.btn_console_warning = QPushButton(self.sa_content)
        self.btn_console_warning.setObjectName(u"btn_console_warning")
        self.btn_console_warning.setCheckable(True)

        self.lyt_console_buttons.addWidget(self.btn_console_warning, 0, 1, 1, 1)

        self.btn_console_success = QPushButton(self.sa_content)
        self.btn_console_success.setObjectName(u"btn_console_success")
        self.btn_console_success.setCheckable(True)

        self.lyt_console_buttons.addWidget(self.btn_console_success, 0, 2, 1, 1)

        self.btn_console_error = QPushButton(self.sa_content)
        self.btn_console_error.setObjectName(u"btn_console_error")
        self.btn_console_error.setCheckable(True)

        self.lyt_console_buttons.addWidget(self.btn_console_error, 0, 3, 1, 1)

        self.btn_console_debug = QPushButton(self.sa_content)
        self.btn_console_debug.setObjectName(u"btn_console_debug")
        self.btn_console_debug.setCheckable(True)

        self.lyt_console_buttons.addWidget(self.btn_console_debug, 0, 4, 1, 1)


        self.lyt_console_section.addLayout(self.lyt_console_buttons)

        self.lyt_console_colors = QHBoxLayout()
        self.lyt_console_colors.setObjectName(u"lyt_console_colors")
        self.lbl_console_colors = QLabel(self.sa_content)
        self.lbl_console_colors.setObjectName(u"lbl_console_colors")
        sizePolicy.setHeightForWidth(self.lbl_console_colors.sizePolicy().hasHeightForWidth())
        self.lbl_console_colors.setSizePolicy(sizePolicy)

        self.lyt_console_colors.addWidget(self.lbl_console_colors)

        self.cb_console_colors = QComboBox(self.sa_content)
        self.cb_console_colors.addItem("")
        self.cb_console_colors.addItem("")
        self.cb_console_colors.setObjectName(u"cb_console_colors")

        self.lyt_console_colors.addWidget(self.cb_console_colors)


        self.lyt_console_section.addLayout(self.lyt_console_colors)


        self.lyt_scroll.addLayout(self.lyt_console_section)

        self.lbl_file_header = QLabel(self.sa_content)
        self.lbl_file_header.setObjectName(u"lbl_file_header")
        self.lbl_file_header.setFont(font)

        self.lyt_scroll.addWidget(self.lbl_file_header)

        self.lyt_file_enabled = QHBoxLayout()
        self.lyt_file_enabled.setObjectName(u"lyt_file_enabled")
        self.lbl_file_enabled = QLabel(self.sa_content)
        self.lbl_file_enabled.setObjectName(u"lbl_file_enabled")
        sizePolicy.setHeightForWidth(self.lbl_file_enabled.sizePolicy().hasHeightForWidth())
        self.lbl_file_enabled.setSizePolicy(sizePolicy)

        self.lyt_file_enabled.addWidget(self.lbl_file_enabled)

        self.cb_file_enabled = QComboBox(self.sa_content)
        self.cb_file_enabled.addItem("")
        self.cb_file_enabled.addItem("")
        self.cb_file_enabled.setObjectName(u"cb_file_enabled")

        self.lyt_file_enabled.addWidget(self.cb_file_enabled)


        self.lyt_scroll.addLayout(self.lyt_file_enabled)

        self.lyt_file_buttons = QGridLayout()
        self.lyt_file_buttons.setObjectName(u"lyt_file_buttons")
        self.btn_file_info = QPushButton(self.sa_content)
        self.btn_file_info.setObjectName(u"btn_file_info")
        self.btn_file_info.setCheckable(True)

        self.lyt_file_buttons.addWidget(self.btn_file_info, 0, 0, 1, 1)

        self.btn_file_warning = QPushButton(self.sa_content)
        self.btn_file_warning.setObjectName(u"btn_file_warning")
        self.btn_file_warning.setCheckable(True)

        self.lyt_file_buttons.addWidget(self.btn_file_warning, 0, 1, 1, 1)

        self.btn_file_success = QPushButton(self.sa_content)
        self.btn_file_success.setObjectName(u"btn_file_success")
        self.btn_file_success.setCheckable(True)

        self.lyt_file_buttons.addWidget(self.btn_file_success, 0, 2, 1, 1)

        self.btn_file_error = QPushButton(self.sa_content)
        self.btn_file_error.setObjectName(u"btn_file_error")
        self.btn_file_error.setCheckable(True)

        self.lyt_file_buttons.addWidget(self.btn_file_error, 0, 3, 1, 1)

        self.btn_file_debug = QPushButton(self.sa_content)
        self.btn_file_debug.setObjectName(u"btn_file_debug")
        self.btn_file_debug.setCheckable(True)

        self.lyt_file_buttons.addWidget(self.btn_file_debug, 0, 4, 1, 1)


        self.lyt_scroll.addLayout(self.lyt_file_buttons)

        self.lyt_file_rotation = QHBoxLayout()
        self.lyt_file_rotation.setObjectName(u"lyt_file_rotation")
        self.lbl_file_rotation = QLabel(self.sa_content)
        self.lbl_file_rotation.setObjectName(u"lbl_file_rotation")
        sizePolicy.setHeightForWidth(self.lbl_file_rotation.sizePolicy().hasHeightForWidth())
        self.lbl_file_rotation.setSizePolicy(sizePolicy)

        self.lyt_file_rotation.addWidget(self.lbl_file_rotation)

        self.sb_file_rotation = QSpinBox(self.sa_content)
        self.sb_file_rotation.setObjectName(u"sb_file_rotation")
        self.sb_file_rotation.setMinimum(1)
        self.sb_file_rotation.setMaximum(512)

        self.lyt_file_rotation.addWidget(self.sb_file_rotation)


        self.lyt_scroll.addLayout(self.lyt_file_rotation)

        self.lyt_file_retention = QHBoxLayout()
        self.lyt_file_retention.setObjectName(u"lyt_file_retention")
        self.lbl_file_retention = QLabel(self.sa_content)
        self.lbl_file_retention.setObjectName(u"lbl_file_retention")
        sizePolicy.setHeightForWidth(self.lbl_file_retention.sizePolicy().hasHeightForWidth())
        self.lbl_file_retention.setSizePolicy(sizePolicy)

        self.lyt_file_retention.addWidget(self.lbl_file_retention)

        self.sb_file_retention = QSpinBox(self.sa_content)
        self.sb_file_retention.setObjectName(u"sb_file_retention")
        self.sb_file_retention.setMinimum(1)
        self.sb_file_retention.setMaximum(365)

        self.lyt_file_retention.addWidget(self.sb_file_retention)


        self.lyt_scroll.addLayout(self.lyt_file_retention)

        self.lyt_file_section = QVBoxLayout()
        self.lyt_file_section.setObjectName(u"lyt_file_section")
        self.lyt_file_path = QHBoxLayout()
        self.lyt_file_path.setObjectName(u"lyt_file_path")
        self.lbl_file_path = QLabel(self.sa_content)
        self.lbl_file_path.setObjectName(u"lbl_file_path")

        self.lyt_file_path.addWidget(self.lbl_file_path)

        self.le_file_path = QLineEdit(self.sa_content)
        self.le_file_path.setObjectName(u"le_file_path")
        self.le_file_path.setReadOnly(True)

        self.lyt_file_path.addWidget(self.le_file_path)

        self.btn_file_browse = QPushButton(self.sa_content)
        self.btn_file_browse.setObjectName(u"btn_file_browse")

        self.lyt_file_path.addWidget(self.btn_file_browse)


        self.lyt_file_section.addLayout(self.lyt_file_path)

        self.lyt_file_compression = QHBoxLayout()
        self.lyt_file_compression.setObjectName(u"lyt_file_compression")
        self.lbl_file_compression = QLabel(self.sa_content)
        self.lbl_file_compression.setObjectName(u"lbl_file_compression")
        sizePolicy.setHeightForWidth(self.lbl_file_compression.sizePolicy().hasHeightForWidth())
        self.lbl_file_compression.setSizePolicy(sizePolicy)

        self.lyt_file_compression.addWidget(self.lbl_file_compression)

        self.cb_file_compression = QComboBox(self.sa_content)
        self.cb_file_compression.addItem("")
        self.cb_file_compression.addItem("")
        self.cb_file_compression.addItem("")
        self.cb_file_compression.setObjectName(u"cb_file_compression")

        self.lyt_file_compression.addWidget(self.cb_file_compression)


        self.lyt_file_section.addLayout(self.lyt_file_compression)


        self.lyt_scroll.addLayout(self.lyt_file_section)

        self.spc_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lyt_scroll.addItem(self.spc_bottom)

        self.sa_logger.setWidget(self.sa_content)

        self.lyt_main.addWidget(self.sa_logger)


        self.retranslateUi(LoggingPage)

        QMetaObject.connectSlotsByName(LoggingPage)
    # setupUi

    def retranslateUi(self, LoggingPage):
        LoggingPage.setWindowTitle(QCoreApplication.translate("LoggingPage", u"XyraEngine - Logging Settings", None))
        self.lbl_console_header.setText(QCoreApplication.translate("LoggingPage", u"Console Output Settings", None))
        self.lbl_console_time.setText(QCoreApplication.translate("LoggingPage", u"Show Time: ", None))
        self.cb_console_time.setItemText(0, QCoreApplication.translate("LoggingPage", u"Yes", None))
        self.cb_console_time.setItemText(1, QCoreApplication.translate("LoggingPage", u"No", None))

        self.btn_console_info.setText(QCoreApplication.translate("LoggingPage", u"Info", None))
        self.btn_console_warning.setText(QCoreApplication.translate("LoggingPage", u"Warnings", None))
        self.btn_console_success.setText(QCoreApplication.translate("LoggingPage", u"Success", None))
        self.btn_console_error.setText(QCoreApplication.translate("LoggingPage", u"Errors", None))
        self.btn_console_debug.setText(QCoreApplication.translate("LoggingPage", u"Debug", None))
        self.lbl_console_colors.setText(QCoreApplication.translate("LoggingPage", u"Colorized output: ", None))
        self.cb_console_colors.setItemText(0, QCoreApplication.translate("LoggingPage", u"Yes", None))
        self.cb_console_colors.setItemText(1, QCoreApplication.translate("LoggingPage", u"No", None))

        self.lbl_file_header.setText(QCoreApplication.translate("LoggingPage", u"File Logging Settings", None))
        self.lbl_file_enabled.setText(QCoreApplication.translate("LoggingPage", u"Log into files:", None))
        self.cb_file_enabled.setItemText(0, QCoreApplication.translate("LoggingPage", u"Yes", None))
        self.cb_file_enabled.setItemText(1, QCoreApplication.translate("LoggingPage", u"No", None))

        self.btn_file_info.setText(QCoreApplication.translate("LoggingPage", u"Info", None))
        self.btn_file_warning.setText(QCoreApplication.translate("LoggingPage", u"Warnings", None))
        self.btn_file_success.setText(QCoreApplication.translate("LoggingPage", u"Success", None))
        self.btn_file_error.setText(QCoreApplication.translate("LoggingPage", u"Errors", None))
        self.btn_file_debug.setText(QCoreApplication.translate("LoggingPage", u"Debug", None))
        self.lbl_file_rotation.setText(QCoreApplication.translate("LoggingPage", u"File rotation (MB): ", None))
        self.sb_file_rotation.setSuffix(QCoreApplication.translate("LoggingPage", u" MB (min 1MB, max 512 MB)", None))
        self.lbl_file_retention.setText(QCoreApplication.translate("LoggingPage", u"Retention (days): ", None))
        self.sb_file_retention.setSuffix(QCoreApplication.translate("LoggingPage", u" Days", None))
        self.lbl_file_path.setText(QCoreApplication.translate("LoggingPage", u"Logs Folder:", None))
        self.le_file_path.setPlaceholderText(QCoreApplication.translate("LoggingPage", u"./logs", None))
        self.btn_file_browse.setText(QCoreApplication.translate("LoggingPage", u"...", None))
        self.lbl_file_compression.setText(QCoreApplication.translate("LoggingPage", u"Compress old logs (ZIP):", None))
        self.cb_file_compression.setItemText(0, QCoreApplication.translate("LoggingPage", u"None", None))
        self.cb_file_compression.setItemText(1, QCoreApplication.translate("LoggingPage", u"zip", None))
        self.cb_file_compression.setItemText(2, QCoreApplication.translate("LoggingPage", u"tar.gz", None))

    # retranslateUi

