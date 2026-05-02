# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThemePreview.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_ThemePreview(object):
    def setupUi(self, ThemePreview):
        if not ThemePreview.objectName():
            ThemePreview.setObjectName(u"ThemePreview")
        ThemePreview.resize(600, 800)
        self.lay_main = QVBoxLayout(ThemePreview)
        self.lay_main.setSpacing(0)
        self.lay_main.setContentsMargins(0, 0, 0, 0)
        self.lay_main.setObjectName(u"lay_main")
        self.grp_state_sim = QGroupBox(ThemePreview)
        self.grp_state_sim.setObjectName(u"grp_state_sim")
        self.grp_state_sim.setAlignment(Qt.AlignCenter)
        self.lay_state_sim = QHBoxLayout(self.grp_state_sim)
        self.lay_state_sim.setObjectName(u"lay_state_sim")
        self.rad_active = QRadioButton(self.grp_state_sim)
        self.rad_active.setObjectName(u"rad_active")
        self.rad_active.setChecked(True)

        self.lay_state_sim.addWidget(self.rad_active)

        self.rad_disabled = QRadioButton(self.grp_state_sim)
        self.rad_disabled.setObjectName(u"rad_disabled")

        self.lay_state_sim.addWidget(self.rad_disabled)


        self.lay_main.addWidget(self.grp_state_sim)

        self.sa_preview = QScrollArea(ThemePreview)
        self.sa_preview.setObjectName(u"sa_preview")
        self.sa_preview.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(0, 0, 598, 712))
        self.lay_preview_content = QVBoxLayout(self.scrollContent)
        self.lay_preview_content.setObjectName(u"lay_preview_content")
        self.grp_buttons = QGroupBox(self.scrollContent)
        self.grp_buttons.setObjectName(u"grp_buttons")
        self.lay_buttons = QVBoxLayout(self.grp_buttons)
        self.lay_buttons.setObjectName(u"lay_buttons")
        self.btn_normal = QPushButton(self.grp_buttons)
        self.btn_normal.setObjectName(u"btn_normal")

        self.lay_buttons.addWidget(self.btn_normal)

        self.btn_flat = QPushButton(self.grp_buttons)
        self.btn_flat.setObjectName(u"btn_flat")
        self.btn_flat.setFlat(True)

        self.lay_buttons.addWidget(self.btn_flat)

        self.l_link = QLabel(self.grp_buttons)
        self.l_link.setObjectName(u"l_link")

        self.lay_buttons.addWidget(self.l_link)


        self.lay_preview_content.addWidget(self.grp_buttons)

        self.grp_inputs = QGroupBox(self.scrollContent)
        self.grp_inputs.setObjectName(u"grp_inputs")
        self.lay_form = QFormLayout(self.grp_inputs)
        self.lay_form.setObjectName(u"lay_form")
        self.l_line_edit = QLabel(self.grp_inputs)
        self.l_line_edit.setObjectName(u"l_line_edit")

        self.lay_form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_line_edit)

        self.edt_input = QLineEdit(self.grp_inputs)
        self.edt_input.setObjectName(u"edt_input")

        self.lay_form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edt_input)

        self.l_combo = QLabel(self.grp_inputs)
        self.l_combo.setObjectName(u"l_combo")

        self.lay_form.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_combo)

        self.cb_options = QComboBox(self.grp_inputs)
        self.cb_options.addItem("")
        self.cb_options.addItem("")
        self.cb_options.setObjectName(u"cb_options")

        self.lay_form.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cb_options)

        self.l_spin = QLabel(self.grp_inputs)
        self.l_spin.setObjectName(u"l_spin")

        self.lay_form.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l_spin)

        self.sb_value = QSpinBox(self.grp_inputs)
        self.sb_value.setObjectName(u"sb_value")

        self.lay_form.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sb_value)


        self.lay_preview_content.addWidget(self.grp_inputs)

        self.grp_selection = QGroupBox(self.scrollContent)
        self.grp_selection.setObjectName(u"grp_selection")
        self.lay_selection = QVBoxLayout(self.grp_selection)
        self.lay_selection.setObjectName(u"lay_selection")
        self.chk_element = QCheckBox(self.grp_selection)
        self.chk_element.setObjectName(u"chk_element")
        self.chk_element.setChecked(True)

        self.lay_selection.addWidget(self.chk_element)

        self.rad_element = QRadioButton(self.grp_selection)
        self.rad_element.setObjectName(u"rad_element")

        self.lay_selection.addWidget(self.rad_element)

        self.lst_widget = QListWidget(self.grp_selection)
        QListWidgetItem(self.lst_widget)
        QListWidgetItem(self.lst_widget)
        self.lst_widget.setObjectName(u"lst_widget")

        self.lay_selection.addWidget(self.lst_widget)


        self.lay_preview_content.addWidget(self.grp_selection)

        self.grp_progress = QGroupBox(self.scrollContent)
        self.grp_progress.setObjectName(u"grp_progress")
        self.lay_progress = QVBoxLayout(self.grp_progress)
        self.lay_progress.setObjectName(u"lay_progress")
        self.prg_bar = QProgressBar(self.grp_progress)
        self.prg_bar.setObjectName(u"prg_bar")
        self.prg_bar.setValue(75)

        self.lay_progress.addWidget(self.prg_bar)

        self.sld_horizontal = QSlider(self.grp_progress)
        self.sld_horizontal.setObjectName(u"sld_horizontal")
        self.sld_horizontal.setOrientation(Qt.Horizontal)

        self.lay_progress.addWidget(self.sld_horizontal)


        self.lay_preview_content.addWidget(self.grp_progress)

        self.sa_preview.setWidget(self.scrollContent)

        self.lay_main.addWidget(self.sa_preview)

        self.buttonBox = QDialogButtonBox(ThemePreview)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.lay_main.addWidget(self.buttonBox)


        self.retranslateUi(ThemePreview)

        QMetaObject.connectSlotsByName(ThemePreview)
    # setupUi

    def retranslateUi(self, ThemePreview):
        ThemePreview.setWindowTitle(QCoreApplication.translate("ThemePreview", u"Live Theme Preview", None))
        self.grp_state_sim.setTitle(QCoreApplication.translate("ThemePreview", u"Simulate Widget State", None))
        self.rad_active.setText(QCoreApplication.translate("ThemePreview", u"Active / Normal", None))
        self.rad_disabled.setText(QCoreApplication.translate("ThemePreview", u"Disabled (Grayed Out)", None))
        self.grp_buttons.setTitle(QCoreApplication.translate("ThemePreview", u"Buttons & Links", None))
        self.btn_normal.setText(QCoreApplication.translate("ThemePreview", u"Standard PushButton", None))
        self.btn_flat.setText(QCoreApplication.translate("ThemePreview", u"Flat Button", None))
        self.l_link.setText(QCoreApplication.translate("ThemePreview", u"<a href=\"#\">Hyperlink Text</a>", None))
        self.grp_inputs.setTitle(QCoreApplication.translate("ThemePreview", u"Input Widgets", None))
        self.l_line_edit.setText(QCoreApplication.translate("ThemePreview", u"Line Edit:", None))
        self.edt_input.setPlaceholderText(QCoreApplication.translate("ThemePreview", u"Placeholder text...", None))
        self.l_combo.setText(QCoreApplication.translate("ThemePreview", u"Combo Box:", None))
        self.cb_options.setItemText(0, QCoreApplication.translate("ThemePreview", u"Option 1", None))
        self.cb_options.setItemText(1, QCoreApplication.translate("ThemePreview", u"Option 2", None))

        self.l_spin.setText(QCoreApplication.translate("ThemePreview", u"Spin Box:", None))
        self.grp_selection.setTitle(QCoreApplication.translate("ThemePreview", u"Selection & Views", None))
        self.chk_element.setText(QCoreApplication.translate("ThemePreview", u"Checkbox Element", None))
        self.rad_element.setText(QCoreApplication.translate("ThemePreview", u"Radio Button Element", None))

        __sortingEnabled = self.lst_widget.isSortingEnabled()
        self.lst_widget.setSortingEnabled(False)
        ___qlistwidgetitem = self.lst_widget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ThemePreview", u"Selected Item (Highlight)", None))
        ___qlistwidgetitem1 = self.lst_widget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ThemePreview", u"Normal Item", None))
        self.lst_widget.setSortingEnabled(__sortingEnabled)

        self.grp_progress.setTitle(QCoreApplication.translate("ThemePreview", u"Containers & Feedback", None))
    # retranslateUi

