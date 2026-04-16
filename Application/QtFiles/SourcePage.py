# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SourcePage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_sourcePage(object):
    def setupUi(self, sourcePage):
        if not sourcePage.objectName():
            sourcePage.setObjectName(u"sourcePage")
        sourcePage.resize(650, 1000)
        self.mainLayout = QVBoxLayout(sourcePage)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.sa_source_code = QScrollArea(sourcePage)
        self.sa_source_code.setObjectName(u"sa_source_code")
        self.sa_source_code.setFrameShape(QFrame.NoFrame)
        self.sa_source_code.setWidgetResizable(True)
        self.sourceCodeScrollContent = QWidget()
        self.sourceCodeScrollContent.setObjectName(u"sourceCodeScrollContent")
        self.sourceCodeScrollContent.setGeometry(QRect(0, 0, 650, 1000))
        self.sourceCodeScrollLayout = QVBoxLayout(self.sourceCodeScrollContent)
        self.sourceCodeScrollLayout.setSpacing(20)
        self.sourceCodeScrollLayout.setContentsMargins(15, 15, 15, 15)
        self.sourceCodeScrollLayout.setObjectName(u"sourceCodeScrollLayout")
        self.l_pre = QLabel(self.sourceCodeScrollContent)
        self.l_pre.setObjectName(u"l_pre")

        self.sourceCodeScrollLayout.addWidget(self.l_pre)

        self.te_preview = QTextEdit(self.sourceCodeScrollContent)
        self.te_preview.setObjectName(u"te_preview")
        self.te_preview.setMinimumSize(QSize(0, 140))
        self.te_preview.setReadOnly(True)

        self.sourceCodeScrollLayout.addWidget(self.te_preview)

        self.l_syn = QLabel(self.sourceCodeScrollContent)
        self.l_syn.setObjectName(u"l_syn")

        self.sourceCodeScrollLayout.addWidget(self.l_syn)

        self.grid_syntax = QGridLayout()
        self.grid_syntax.setObjectName(u"grid_syntax")
        self.btn_sel_tags = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_tags.setObjectName(u"btn_sel_tags")
        self.btn_sel_tags.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_tags, 0, 0, 1, 1)

        self.btn_sel_attrs = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_attrs.setObjectName(u"btn_sel_attrs")
        self.btn_sel_attrs.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_attrs, 0, 1, 1, 1)

        self.btn_sel_strings = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_strings.setObjectName(u"btn_sel_strings")
        self.btn_sel_strings.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_strings, 1, 0, 1, 1)

        self.btn_sel_comments = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_comments.setObjectName(u"btn_sel_comments")
        self.btn_sel_comments.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_comments, 1, 1, 1, 1)

        self.btn_sel_keywords = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_keywords.setObjectName(u"btn_sel_keywords")
        self.btn_sel_keywords.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_keywords, 2, 0, 1, 1)

        self.btn_sel_variables = QPushButton(self.sourceCodeScrollContent)
        self.btn_sel_variables.setObjectName(u"btn_sel_variables")
        self.btn_sel_variables.setCheckable(True)

        self.grid_syntax.addWidget(self.btn_sel_variables, 2, 1, 1, 1)


        self.sourceCodeScrollLayout.addLayout(self.grid_syntax)

        self.lay_tools = QHBoxLayout()
        self.lay_tools.setObjectName(u"lay_tools")
        self.btn_style_color = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_color.setObjectName(u"btn_style_color")

        self.lay_tools.addWidget(self.btn_style_color)

        self.btn_style_bold = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_bold.setObjectName(u"btn_style_bold")
        self.btn_style_bold.setCheckable(True)

        self.lay_tools.addWidget(self.btn_style_bold)

        self.btn_style_italic = QPushButton(self.sourceCodeScrollContent)
        self.btn_style_italic.setObjectName(u"btn_style_italic")
        self.btn_style_italic.setCheckable(True)

        self.lay_tools.addWidget(self.btn_style_italic)

        self.cb_style_transform = QComboBox(self.sourceCodeScrollContent)
        self.cb_style_transform.addItem("")
        self.cb_style_transform.addItem("")
        self.cb_style_transform.addItem("")
        self.cb_style_transform.setObjectName(u"cb_style_transform")

        self.lay_tools.addWidget(self.cb_style_transform)


        self.sourceCodeScrollLayout.addLayout(self.lay_tools)

        self.l_beh = QLabel(self.sourceCodeScrollContent)
        self.l_beh.setObjectName(u"l_beh")

        self.sourceCodeScrollLayout.addWidget(self.l_beh)

        self.grid_beh = QGridLayout()
        self.grid_beh.setObjectName(u"grid_beh")
        self.l_t = QLabel(self.sourceCodeScrollContent)
        self.l_t.setObjectName(u"l_t")

        self.grid_beh.addWidget(self.l_t, 0, 0, 1, 1)

        self.sb_tab_size = QSpinBox(self.sourceCodeScrollContent)
        self.sb_tab_size.setObjectName(u"sb_tab_size")
        self.sb_tab_size.setValue(4)

        self.grid_beh.addWidget(self.sb_tab_size, 0, 1, 1, 1)

        self.l_i = QLabel(self.sourceCodeScrollContent)
        self.l_i.setObjectName(u"l_i")

        self.grid_beh.addWidget(self.l_i, 1, 0, 1, 1)

        self.cb_indent_style = QComboBox(self.sourceCodeScrollContent)
        self.cb_indent_style.addItem("")
        self.cb_indent_style.addItem("")
        self.cb_indent_style.setObjectName(u"cb_indent_style")

        self.grid_beh.addWidget(self.cb_indent_style, 1, 1, 1, 1)

        self.l_cur = QLabel(self.sourceCodeScrollContent)
        self.l_cur.setObjectName(u"l_cur")

        self.grid_beh.addWidget(self.l_cur, 2, 0, 1, 1)

        self.cb_cursor_style = QComboBox(self.sourceCodeScrollContent)
        self.cb_cursor_style.addItem("")
        self.cb_cursor_style.addItem("")
        self.cb_cursor_style.addItem("")
        self.cb_cursor_style.setObjectName(u"cb_cursor_style")

        self.grid_beh.addWidget(self.cb_cursor_style, 2, 1, 1, 1)


        self.sourceCodeScrollLayout.addLayout(self.grid_beh)

        self.lay_feat = QVBoxLayout()
        self.lay_feat.setSpacing(8)
        self.lay_feat.setObjectName(u"lay_feat")
        self.chk_line_numbers = QCheckBox(self.sourceCodeScrollContent)
        self.chk_line_numbers.setObjectName(u"chk_line_numbers")

        self.lay_feat.addWidget(self.chk_line_numbers)

        self.chk_highlight_line = QCheckBox(self.sourceCodeScrollContent)
        self.chk_highlight_line.setObjectName(u"chk_highlight_line")

        self.lay_feat.addWidget(self.chk_highlight_line)

        self.chk_match_brackets = QCheckBox(self.sourceCodeScrollContent)
        self.chk_match_brackets.setObjectName(u"chk_match_brackets")

        self.lay_feat.addWidget(self.chk_match_brackets)

        self.chk_indent_guides = QCheckBox(self.sourceCodeScrollContent)
        self.chk_indent_guides.setObjectName(u"chk_indent_guides")

        self.lay_feat.addWidget(self.chk_indent_guides)

        self.chk_word_wrap = QCheckBox(self.sourceCodeScrollContent)
        self.chk_word_wrap.setObjectName(u"chk_word_wrap")

        self.lay_feat.addWidget(self.chk_word_wrap)

        self.chk_minimap = QCheckBox(self.sourceCodeScrollContent)
        self.chk_minimap.setObjectName(u"chk_minimap")

        self.lay_feat.addWidget(self.chk_minimap)

        self.chk_auto_close = QCheckBox(self.sourceCodeScrollContent)
        self.chk_auto_close.setObjectName(u"chk_auto_close")

        self.lay_feat.addWidget(self.chk_auto_close)

        self.chk_whitespace = QCheckBox(self.sourceCodeScrollContent)
        self.chk_whitespace.setObjectName(u"chk_whitespace")

        self.lay_feat.addWidget(self.chk_whitespace)

        self.chk_format_save = QCheckBox(self.sourceCodeScrollContent)
        self.chk_format_save.setObjectName(u"chk_format_save")

        self.lay_feat.addWidget(self.chk_format_save)


        self.sourceCodeScrollLayout.addLayout(self.lay_feat)

        self.v_sp = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sourceCodeScrollLayout.addItem(self.v_sp)

        self.sa_source_code.setWidget(self.sourceCodeScrollContent)

        self.mainLayout.addWidget(self.sa_source_code)


        self.retranslateUi(sourcePage)

        QMetaObject.connectSlotsByName(sourcePage)
    # setupUi

    def retranslateUi(self, sourcePage):
        self.l_pre.setText(QCoreApplication.translate("sourcePage", u"<b>Editor Preview</b>", None))
        self.te_preview.setHtml(QCoreApplication.translate("sourcePage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;div style=&quot;font-family: 'Consolas', 'Monaco', monospace; line-height: 1.4; font-size: 13px;&quot;&gt; &lt;span style=&quot;color: #569cd6;&quot;&gt;&amp;lt;div&lt;/span&gt; &lt;span style=&quot;color: #9cdcfe;&quot;&gt;class&lt;/span&gt;=&lt;span style=&quot;color: #ce9178;&quot;&gt;&quot;card&quot;&lt;/span&gt; &lt;span style=&quot;color: #9cdcfe;&quot;&gt;id&lt;/span&gt;=&lt;span style=&quot"
                        ";color: #ce9178;&quot;&gt;&quot;hero&quot;&lt;/span&gt;&lt;span style=&quot;color: #569cd6;&quot;&gt;&amp;gt;&lt;/span&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color: #569cd6;&quot;&gt;&amp;lt;h1&amp;gt;&lt;/span&gt;Xyra Editor&lt;span style=&quot;color: #569cd6;&quot;&gt;&amp;lt;/h1&amp;gt;&lt;/span&gt; &lt;br&gt;&lt;span style=&quot;color: #569cd6;&quot;&gt;&amp;lt;/div&amp;gt;&lt;/span&gt;&lt;br&gt; &lt;br&gt;&lt;span style=&quot;color: #6a9955;&quot;&gt;/* CSS: Selektory a Vlastnosti */&lt;/span&gt;&lt;br&gt; &lt;span style=&quot;color: #d7ba7d;&quot;&gt;.card&lt;/span&gt; { &lt;br&gt;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color: #9cdcfe;&quot;&gt;color&lt;/span&gt;: &lt;span style=&quot;color: #b5cea8;&quot;&gt;#ffffff&lt;/span&gt;; &lt;br&gt;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color: #9cdcfe;&quot;&gt;display&lt;/span&gt;: &lt;span style=&quot;color: #ce9178;&quot;&gt;flex&lt;/span&gt;; &lt;br&gt;}&lt;br&gt; &lt;br&gt;&lt;span style=&quot;color: #6a9955;&quot;&gt;// JS: Kl\u00ed\u010d"
                        "ov\u00e1 slova a Prom\u011bnn\u00e9&lt;/span&gt;&lt;br&gt; &lt;span style=&quot;color: #569cd6;&quot;&gt;const&lt;/span&gt; &lt;span style=&quot;color: #4fc1ff;&quot;&gt;app&lt;/span&gt; = &lt;span style=&quot;color: #569cd6;&quot;&gt;new&lt;/span&gt; &lt;span style=&quot;color: #dcdcaa;&quot;&gt;Editor&lt;/span&gt;({ &lt;br&gt;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color: #9cdcfe;&quot;&gt;active&lt;/span&gt;: &lt;span style=&quot;color: #569cd6;&quot;&gt;true&lt;/span&gt;, &lt;br&gt;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color: #9cdcfe;&quot;&gt;version&lt;/span&gt;: &lt;span style=&quot;color: #b5cea8;&quot;&gt;2.0&lt;/span&gt; &lt;br&gt;});</p></body></html>", None))
        self.l_syn.setText(QCoreApplication.translate("sourcePage", u"<b>Syntax Highlighting</b>", None))
        self.btn_sel_tags.setText(QCoreApplication.translate("sourcePage", u"HTML Tags", None))
        self.btn_sel_attrs.setText(QCoreApplication.translate("sourcePage", u"Attributes", None))
        self.btn_sel_strings.setText(QCoreApplication.translate("sourcePage", u"Strings", None))
        self.btn_sel_comments.setText(QCoreApplication.translate("sourcePage", u"Comments", None))
        self.btn_sel_keywords.setText(QCoreApplication.translate("sourcePage", u"JS Keywords", None))
        self.btn_sel_variables.setText(QCoreApplication.translate("sourcePage", u"Variables", None))
        self.btn_style_color.setText(QCoreApplication.translate("sourcePage", u"Color", None))
        self.btn_style_bold.setText(QCoreApplication.translate("sourcePage", u"B", None))
        self.btn_style_italic.setText(QCoreApplication.translate("sourcePage", u"I", None))
        self.cb_style_transform.setItemText(0, QCoreApplication.translate("sourcePage", u"No Transform", None))
        self.cb_style_transform.setItemText(1, QCoreApplication.translate("sourcePage", u"UPPERCASE", None))
        self.cb_style_transform.setItemText(2, QCoreApplication.translate("sourcePage", u"lowercase", None))

        self.l_beh.setText(QCoreApplication.translate("sourcePage", u"<b>Editor Behavior</b>", None))
        self.l_t.setText(QCoreApplication.translate("sourcePage", u"Tab Size:", None))
        self.l_i.setText(QCoreApplication.translate("sourcePage", u"Indentation:", None))
        self.cb_indent_style.setItemText(0, QCoreApplication.translate("sourcePage", u"Tabs", None))
        self.cb_indent_style.setItemText(1, QCoreApplication.translate("sourcePage", u"Spaces", None))

        self.l_cur.setText(QCoreApplication.translate("sourcePage", u"Cursor Style:", None))
        self.cb_cursor_style.setItemText(0, QCoreApplication.translate("sourcePage", u"Line (Standard)", None))
        self.cb_cursor_style.setItemText(1, QCoreApplication.translate("sourcePage", u"Block (Retro)", None))
        self.cb_cursor_style.setItemText(2, QCoreApplication.translate("sourcePage", u"Underline", None))

        self.chk_line_numbers.setText(QCoreApplication.translate("sourcePage", u"Show Line Numbers", None))
        self.chk_highlight_line.setText(QCoreApplication.translate("sourcePage", u"Highlight Current Line", None))
        self.chk_match_brackets.setText(QCoreApplication.translate("sourcePage", u"Highlight Matching Brackets", None))
        self.chk_indent_guides.setText(QCoreApplication.translate("sourcePage", u"Show Indentation Guides", None))
        self.chk_word_wrap.setText(QCoreApplication.translate("sourcePage", u"Soft Word Wrap", None))
        self.chk_minimap.setText(QCoreApplication.translate("sourcePage", u"Display Minimap Overview", None))
        self.chk_auto_close.setText(QCoreApplication.translate("sourcePage", u"Auto-close Tags & Brackets", None))
        self.chk_whitespace.setText(QCoreApplication.translate("sourcePage", u"Render Whitespace Symbols", None))
        self.chk_format_save.setText(QCoreApplication.translate("sourcePage", u"Format Document on Save", None))
        pass
    # retranslateUi

