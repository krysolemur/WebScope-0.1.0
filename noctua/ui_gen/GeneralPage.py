# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GeneralPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_GeneralPage(object):
    def setupUi(self, GeneralPage):
        if not GeneralPage.objectName():
            GeneralPage.setObjectName(u"GeneralPage")
        GeneralPage.resize(900, 1000)
        self.lyt_main = QVBoxLayout(GeneralPage)
        self.lyt_main.setSpacing(3)
        self.lyt_main.setObjectName(u"lyt_main")
        self.lyt_main.setContentsMargins(3, 3, 3, 3)
        self.sa_general = QScrollArea(GeneralPage)
        self.sa_general.setObjectName(u"sa_general")
        self.sa_general.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_general.setWidgetResizable(True)
        self.sa_content = QWidget()
        self.sa_content.setObjectName(u"sa_content")
        self.sa_content.setGeometry(QRect(0, 0, 892, 992))
        self.lyt_scroll = QVBoxLayout(self.sa_content)
        self.lyt_scroll.setObjectName(u"lyt_scroll")
        self.lbl_appearance_header = QLabel(self.sa_content)
        self.lbl_appearance_header.setObjectName(u"lbl_appearance_header")
        font = QFont()
        font.setBold(True)
        self.lbl_appearance_header.setFont(font)

        self.lyt_scroll.addWidget(self.lbl_appearance_header)

        self.lyt_appearance = QGridLayout()
        self.lyt_appearance.setObjectName(u"lyt_appearance")
        self.cb_gen_theme = QComboBox(self.sa_content)
        self.cb_gen_theme.addItem("")
        self.cb_gen_theme.addItem("")
        self.cb_gen_theme.addItem("")
        self.cb_gen_theme.setObjectName(u"cb_gen_theme")

        self.lyt_appearance.addWidget(self.cb_gen_theme, 0, 1, 1, 1)

        self.lbl_gen_font = QLabel(self.sa_content)
        self.lbl_gen_font.setObjectName(u"lbl_gen_font")

        self.lyt_appearance.addWidget(self.lbl_gen_font, 1, 0, 1, 1)

        self.cb_gen_font_size = QComboBox(self.sa_content)
        self.cb_gen_font_size.addItem("")
        self.cb_gen_font_size.addItem("")
        self.cb_gen_font_size.addItem("")
        self.cb_gen_font_size.setObjectName(u"cb_gen_font_size")

        self.lyt_appearance.addWidget(self.cb_gen_font_size, 2, 1, 1, 2)

        self.btn_gen_theme = QPushButton(self.sa_content)
        self.btn_gen_theme.setObjectName(u"btn_gen_theme")

        self.lyt_appearance.addWidget(self.btn_gen_theme, 0, 2, 1, 1)

        self.lbl_gen_font_size = QLabel(self.sa_content)
        self.lbl_gen_font_size.setObjectName(u"lbl_gen_font_size")

        self.lyt_appearance.addWidget(self.lbl_gen_font_size, 2, 0, 1, 1)

        self.lbl_gen_theme = QLabel(self.sa_content)
        self.lbl_gen_theme.setObjectName(u"lbl_gen_theme")

        self.lyt_appearance.addWidget(self.lbl_gen_theme, 0, 0, 1, 1)

        self.lbl_gen_stylesheet = QLabel(self.sa_content)
        self.lbl_gen_stylesheet.setObjectName(u"lbl_gen_stylesheet")

        self.lyt_appearance.addWidget(self.lbl_gen_stylesheet, 3, 0, 1, 1)

        self.btn_gen_stylesheet = QPushButton(self.sa_content)
        self.btn_gen_stylesheet.setObjectName(u"btn_gen_stylesheet")

        self.lyt_appearance.addWidget(self.btn_gen_stylesheet, 3, 2, 1, 1)

        self.cb_gen_stylesheet = QComboBox(self.sa_content)
        self.cb_gen_stylesheet.addItem("")
        self.cb_gen_stylesheet.setObjectName(u"cb_gen_stylesheet")

        self.lyt_appearance.addWidget(self.cb_gen_stylesheet, 3, 1, 1, 1)

        self.fcb_gen_font = QFontComboBox(self.sa_content)
        self.fcb_gen_font.setObjectName(u"fcb_gen_font")

        self.lyt_appearance.addWidget(self.fcb_gen_font, 1, 1, 1, 2)


        self.lyt_scroll.addLayout(self.lyt_appearance)

        self.lbl_advanced_header = QLabel(self.sa_content)
        self.lbl_advanced_header.setObjectName(u"lbl_advanced_header")
        self.lbl_advanced_header.setFont(font)

        self.lyt_scroll.addWidget(self.lbl_advanced_header)

        self.lyt_advanced_options = QVBoxLayout()
        self.lyt_advanced_options.setObjectName(u"lyt_advanced_options")
        self.lyt_adv_autosave = QHBoxLayout()
        self.lyt_adv_autosave.setObjectName(u"lyt_adv_autosave")
        self.lbl_adv_autosave = QLabel(self.sa_content)
        self.lbl_adv_autosave.setObjectName(u"lbl_adv_autosave")

        self.lyt_adv_autosave.addWidget(self.lbl_adv_autosave)

        self.sb_adv_autosave_interval = QSpinBox(self.sa_content)
        self.sb_adv_autosave_interval.setObjectName(u"sb_adv_autosave_interval")
        self.sb_adv_autosave_interval.setMinimum(1)
        self.sb_adv_autosave_interval.setMaximum(60)
        self.sb_adv_autosave_interval.setValue(5)

        self.lyt_adv_autosave.addWidget(self.sb_adv_autosave_interval)


        self.lyt_advanced_options.addLayout(self.lyt_adv_autosave)

        self.chk_adv_gpu = QCheckBox(self.sa_content)
        self.chk_adv_gpu.setObjectName(u"chk_adv_gpu")
        self.chk_adv_gpu.setChecked(True)

        self.lyt_advanced_options.addWidget(self.chk_adv_gpu)

        self.lyt_adv_startup = QHBoxLayout()
        self.lyt_adv_startup.setObjectName(u"lyt_adv_startup")
        self.lbl_adv_startup = QLabel(self.sa_content)
        self.lbl_adv_startup.setObjectName(u"lbl_adv_startup")

        self.lyt_adv_startup.addWidget(self.lbl_adv_startup)

        self.cb_adv_startup = QComboBox(self.sa_content)
        self.cb_adv_startup.addItem("")
        self.cb_adv_startup.addItem("")
        self.cb_adv_startup.addItem("")
        self.cb_adv_startup.setObjectName(u"cb_adv_startup")

        self.lyt_adv_startup.addWidget(self.cb_adv_startup)


        self.lyt_advanced_options.addLayout(self.lyt_adv_startup)


        self.lyt_scroll.addLayout(self.lyt_advanced_options)

        self.lbl_system_header = QLabel(self.sa_content)
        self.lbl_system_header.setObjectName(u"lbl_system_header")
        self.lbl_system_header.setFont(font)

        self.lyt_scroll.addWidget(self.lbl_system_header)

        self.lyt_system = QVBoxLayout()
        self.lyt_system.setObjectName(u"lyt_system")
        self.chk_sys_updates = QCheckBox(self.sa_content)
        self.chk_sys_updates.setObjectName(u"chk_sys_updates")
        self.chk_sys_updates.setChecked(True)

        self.lyt_system.addWidget(self.chk_sys_updates)

        self.chk_sys_telemetry = QCheckBox(self.sa_content)
        self.chk_sys_telemetry.setObjectName(u"chk_sys_telemetry")

        self.lyt_system.addWidget(self.chk_sys_telemetry)

        self.lyt_sys_lang = QHBoxLayout()
        self.lyt_sys_lang.setObjectName(u"lyt_sys_lang")
        self.lbl_sys_lang = QLabel(self.sa_content)
        self.lbl_sys_lang.setObjectName(u"lbl_sys_lang")

        self.lyt_sys_lang.addWidget(self.lbl_sys_lang)

        self.cb_sys_lang = QComboBox(self.sa_content)
        self.cb_sys_lang.addItem("")
        self.cb_sys_lang.addItem("")
        self.cb_sys_lang.setObjectName(u"cb_sys_lang")

        self.lyt_sys_lang.addWidget(self.cb_sys_lang)


        self.lyt_system.addLayout(self.lyt_sys_lang)


        self.lyt_scroll.addLayout(self.lyt_system)

        self.spc_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lyt_scroll.addItem(self.spc_bottom)

        self.sa_general.setWidget(self.sa_content)

        self.lyt_main.addWidget(self.sa_general)


        self.retranslateUi(GeneralPage)

        QMetaObject.connectSlotsByName(GeneralPage)
    # setupUi

    def retranslateUi(self, GeneralPage):
        GeneralPage.setWindowTitle(QCoreApplication.translate("GeneralPage", u"XyraEngine - General Settings", None))
        self.lbl_appearance_header.setText(QCoreApplication.translate("GeneralPage", u"Appearance & Interface", None))
        self.cb_gen_theme.setItemText(0, QCoreApplication.translate("GeneralPage", u"Default", None))
        self.cb_gen_theme.setItemText(1, QCoreApplication.translate("GeneralPage", u"Dark", None))
        self.cb_gen_theme.setItemText(2, QCoreApplication.translate("GeneralPage", u"Light", None))

        self.lbl_gen_font.setText(QCoreApplication.translate("GeneralPage", u"Global Font:", None))
        self.cb_gen_font_size.setItemText(0, QCoreApplication.translate("GeneralPage", u"Small", None))
        self.cb_gen_font_size.setItemText(1, QCoreApplication.translate("GeneralPage", u"Medium (recommended)", None))
        self.cb_gen_font_size.setItemText(2, QCoreApplication.translate("GeneralPage", u"Large", None))

        self.btn_gen_theme.setText(QCoreApplication.translate("GeneralPage", u"Add theme", None))
        self.lbl_gen_font_size.setText(QCoreApplication.translate("GeneralPage", u"Font Size:", None))
        self.lbl_gen_theme.setText(QCoreApplication.translate("GeneralPage", u"Application Theme:", None))
        self.lbl_gen_stylesheet.setText(QCoreApplication.translate("GeneralPage", u"Stylesheet:", None))
        self.btn_gen_stylesheet.setText(QCoreApplication.translate("GeneralPage", u"Add stylesheet", None))
        self.cb_gen_stylesheet.setItemText(0, QCoreApplication.translate("GeneralPage", u"Default", None))

        self.lbl_advanced_header.setText(QCoreApplication.translate("GeneralPage", u"Advanced Application Settings", None))
        self.lbl_adv_autosave.setText(QCoreApplication.translate("GeneralPage", u"Auto-save interval:", None))
        self.sb_adv_autosave_interval.setSuffix(QCoreApplication.translate("GeneralPage", u" minutes", None))
        self.chk_adv_gpu.setText(QCoreApplication.translate("GeneralPage", u"Enable Hardware Acceleration (GPU)", None))
        self.lbl_adv_startup.setText(QCoreApplication.translate("GeneralPage", u"On Startup:", None))
        self.cb_adv_startup.setItemText(0, QCoreApplication.translate("GeneralPage", u"Show Dashboard", None))
        self.cb_adv_startup.setItemText(1, QCoreApplication.translate("GeneralPage", u"Load Last Project", None))
        self.cb_adv_startup.setItemText(2, QCoreApplication.translate("GeneralPage", u"Open Empty Project", None))

        self.lbl_system_header.setText(QCoreApplication.translate("GeneralPage", u"System & Privacy", None))
        self.chk_sys_updates.setText(QCoreApplication.translate("GeneralPage", u"Check for updates automatically", None))
        self.chk_sys_telemetry.setText(QCoreApplication.translate("GeneralPage", u"Send anonymous crash reports to help improve XyraEngine", None))
        self.lbl_sys_lang.setText(QCoreApplication.translate("GeneralPage", u"Application Language:", None))
        self.cb_sys_lang.setItemText(0, QCoreApplication.translate("GeneralPage", u"English", None))
        self.cb_sys_lang.setItemText(1, QCoreApplication.translate("GeneralPage", u"Czech", None))

    # retranslateUi

