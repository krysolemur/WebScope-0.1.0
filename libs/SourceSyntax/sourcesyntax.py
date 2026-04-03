# sourcesyntax.py

# Import system files
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor # type: ignore
from PySide6.QtCore import QRegularExpression # type: ignore

# Class source syntax for rules for source code
class SourceSyntax(QSyntaxHighlighter):
    def __init__(self, parent):
        '''
        Init parents and setup some important variables.
        '''

        # Init parents
        super().__init__(parent)

        # Rules list variable
        self.rules = []

        # Create bold elements format
        bold_format = QTextCharFormat()

        # Set bold format 
        bold_format.setFontWeight(QFont.Bold)

        # Red foreground for elemetns
        bold_format.setForeground(QColor("#e06c75")) # Např. jemně červená
        
        # Set only for <something>
        bold_tags = r"<(/?p|/?div|/?h1|/?h2|/?h3|/?strong)\b[^>]*>"

        # Appends it to rules
        self.rules.append((QRegularExpression(bold_tags), bold_format))

        # Create format for others texts
        normal_tag_format = QTextCharFormat()

        # Blue color
        normal_tag_format.setForeground(QColor("#61afef"))

        # For another text
        self.rules.append((QRegularExpression(r"<[^>]+>"), normal_tag_format))

    # Function that highlight html elements
    def highlightBlock(self, text):
        # Seatch through text
        for pattern, format in self.rules:
            # Set format
            match_iterator = pattern.globalMatch(text)

            #
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)