# ErrorDialog.py

import traceback
import sys

from PySide6.QtWidgets import QDialog, QApplication # type: ignore

from noctua.ui_gen.ErrorDialog import Ui_ErrorDialog

class ErrorDialog(QDialog):

    def __init__(self, exception:Exception, msg:str) -> None:

        # Init parents
        super().__init__()

        # Load ui
        self.ui = Ui_ErrorDialog()

        # Setup ui
        self.ui.setupUi(self)

        # Error 
        self.error = self._error_details(exception)

        # Set messsage text
        self.ui.lbl_title.setText(f"{type(exception).__name__}: {str(exception)}")

        # Set error detail text
        self.ui.te_error_details.setHtml(self._format_error(self.error))

        # Copy to clipboard
        self.ui.btn_copy.clicked.connect(self._copy_to_clipboard)

        # Close
        self.ui.btn_close.clicked.connect(self.accept)

        # Show details
        self.ui.btn_details_toggle.toggled.connect(self._toggle_details)

        # Resize and set window title
        self.resize(self.sizeHint())    
        self.setWindowTitle(msg)

    # Get error details
    def _error_details(self, exception) -> dict:
        # Full traceback of error
        full_traceback = traceback.format_exc()
        
        # Error location
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb_last = traceback.extract_tb(exc_tb)[-1] if exc_tb else None
        
        # Details dictonary
        details = {
            # Type and message
            "type": type(exception).__name__,
            "message": str(exception),
            
            # Localize error
            "file": tb_last.filename if tb_last else "Unknown",
            "line": tb_last.lineno if tb_last else "N/A",
            "function": tb_last.name if tb_last else "N/A",
            "code": tb_last.line if tb_last else "N/A",
            
            # Full trackeback
            "full_traceback": full_traceback,
            
            # Special info for some exceptions
            "extra_info": {}
        }

        # Specific errors data
        if isinstance(exception, OSError):
            details["extra_info"]["errno"] = exception.errno
            details["extra_info"]["path"] = exception.filename
        
        # Return details
        return details

    # Copy error to clipboard
    def _copy_to_clipboard(self) -> None:
        # Create app clipboard
        clipboard = QApplication.clipboard()

        # Format text o clipboard
        formatted_text = self._format_error(self.error)
        plain_text = formatted_text.replace("<br>", "\n").replace("&nbsp;", " ")

        # Set text 
        clipboard.setText(plain_text)

    # Toggle details
    def _toggle_details(self, checked) -> None:
        # Set visible by checked
        self.ui.te_error_details.setVisible(checked)
        
        # Change arrow directtion
        self.ui.btn_details_toggle.setText("▼ Hide Details" if checked else "▶ Show Details")
        
        # Resize dialog
        self.resize(self.sizeHint())

    # Format error
    def _format_error(self, error) -> str:
        # Report 
        report = "{<br>"

        # Browse all keys and values
        for key, value in error.items():
            # Add parsed to new report
            clean_value = str(value).replace("\n", "<br>&nbsp;&nbsp;&nbsp;&nbsp;")
        
            report += f"&nbsp;&nbsp;&nbsp;&nbsp;{key}: \"{clean_value}\",<br>"

        # End of report
        report += "}"

        # Return new report
        return report


