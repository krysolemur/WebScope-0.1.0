# Logger.py

from datetime import datetime
import os

from Application.AppContext import ctx

# Default configuration
DEFAULT_CONFIG = {
    "cb_console_time": "Yes",
    "cb_console_colors": "Yes",
    "btn_console_info": True,
    "btn_console_warning": True,
    "btn_console_success": True,
    "btn_console_error": True,
    "btn_console_debug": False,
    "cb_file_enabled": "Yes",
    "btn_file_info": False,
    "btn_file_warning": False,
    "btn_file_success": False,
    "btn_file_error": True,
    "btn_file_debug": False,
    "sb_file_rotation": 10,
    "sb_file_retention": 7,
    "le_file_path": "./Logs",
    "cb_file_compression": "zip"
}

class Logger:

    # Logs dir
    DEFAULT_LOG_DIR = "Logs"
    
    # Logs filepath
    DEFAULT_LOG_FILE = "app.log"

    # Level colors
    LEVEL_COLORS = {
        "INFO": "\033[94m",    # Light blue
        "WARN": "\033[93m",    # Yellow
        "SUCCESS": "\033[92m", # Green
        "ERROR": "\033[91m",   # Red
        "DEBUG": "\033[95m",   # Magenta
        "CRITICAL": "\033[1;41;97m", # Bold white
        "RESET": "\033[0m"     # Reset
    }
    
    def __init__(self, config:dict) -> None:

        self.log = None

        # Create paths
        self.log_dir = config.get("le_file_path", DEFAULT_CONFIG.get("le_file_path", self.DEFAULT_LOG_DIR))
        self.log_path = os.path.join(self.log_dir, self.DEFAULT_LOG_FILE)

        # Get c_levels and f_levels
        self.c_levels = {
            "INFO": config["btn_console_info"],
            "WARN": config["btn_console_warning"],
            "SUCCESS": config["btn_console_success"],
            "ERROR": config["btn_console_error"],
            "DEBUG": config["btn_console_debug"],
            "CRITICAL": True
        }

        if config.get("cb_file_enabled") == "Yes":
            # Set levels for file logging
            self.f_levels = {
                "INFO": config["btn_file_info"],
                "WARN": config["btn_file_warning"],
                "SUCCESS": config["btn_file_success"],
                "ERROR": config["btn_file_error"],
                "DEBUG": config["btn_file_debug"],
                "CRITICAL": True
            }

            # File handling
            try:
                # Check logging directory
                if self.log_dir:
                    os.makedirs(self.log_dir, exist_ok=True)
                self.log = open(self.log_path, "a", encoding="utf-8")
            except OSError as e:
                self.critical(e)
                self.log = None

        else:
            self.f_levels = {
                "INFO": False,
                "WARN": False,
                "SUCCESS": False,
                "ERROR": False,
                "DEBUG": False,
                "CRITICAL": True
            }

        # Get time and colors
        self.time = config.get("cb_console_time") == "Yes"
        self.colored = config.get("cb_console_colors") == "Yes"

        # Log init
        self.info("Logger initialized")

    # Writing to console 
    def _cout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.c_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%H:%M:%S")

        # Create msg
        if self.colored:
            clean_row = f"\033[1;97m{row}\033[0m" if row else ""
            path = f"{filename}{':' if filename else ''}{func}{':' if func else ''}{clean_row}"
            msg = f"\033[93m{timestamp if self.time else ""}\033[0m {self.LEVEL_COLORS[level]}{level:^10}\033[0m {path}{' - ' if path else ''}{msg}"
        else:
            path = f"{filename}{':' if filename else ''}{func}{':' if func else ''}{row}"
            msg = f"{timestamp if self.time else ""} {level:^10} {path}{' - ' if path else ''}{msg}"

        # Print msg
        print(msg)
    
    # Writing to file
    def _fout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.f_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create msg
        path = f"{filename}{':' if filename else ''}{func}{':' if func else ''}{row}"
        msg = f"{timestamp if self.time else ""} {level:^10} {path}{' - ' if path else ''}{msg}"

        # Write msg
        try:
            self.log.write(msg+"\n")
            self.log.flush()
        except OSError as e:
            self.critical(e)
            self.log = None 
    
    # Info log
    def info(self, msg) -> None:
        self._cout("INFO", msg)
        if self.log:
            self._fout("INFO", msg)

    # Warning log
    def warn(self, msg) -> None:
        self._cout("WARN", msg)
        if self.log:
            self._fout("INFO", msg)

    # Success log
    def success(self, msg) -> None:
        self._cout("SUCCESS", msg)
        if self.log:
            self._fout("INFO", msg)
            
    # Error log
    def error(self, msg) -> None:
        import inspect

        # Get info about where was func calling

        # Filename, row and func
        caller_frame = inspect.stack()[1]

        filename = os.path.basename(caller_frame.filename)
        row = caller_frame.lineno
        func = caller_frame.function

        # Output
        self._cout("ERROR", msg, row=row, func=func, filename=filename)
        if self.log:
            self._fout("ERROR", msg, row=row, func=func, filename=filename)

    # Debug log
    def debug(self, msg) -> None:
        self._cout("DEBUG", msg)
        if self.log:
            self._fout("INFO", msg)

    # Critical -> Not in settings
    def critical(self, exception) -> None:
        # Get details from exception
        msg = self._error_details(exception=exception)

        # Output
        self._cout("CRITICAL", msg)
        if self.log:
            self._fout("INFO", msg)

    # Get error details
    @staticmethod
    def _error_details(exception) -> dict:
        import traceback
        import json
        import sys

        # Full traceback of error
        full_traceback = traceback.format_exc()
        
        # Error location
        _, _, exc_tb = sys.exc_info()
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
            "full_traceback": "\n" + full_traceback,
        }

        # Specific errors data
        if isinstance(exception, OSError):
            details["extra_info"]["errno"] = exception.errno
            details["extra_info"]["path"] = exception.filename

        # Format details
        json_string = json.dumps(details, indent=4, ensure_ascii=False)

        ident = " " * 6

        clean_json = json_string.replace('\\n', '\n' + ident)
        clean_json = clean_json.replace('\\"', '"')

        return clean_json

# Init logger
logger = Logger(ctx.config.get("LoggingPage", DEFAULT_CONFIG))

