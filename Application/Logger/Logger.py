# Logger.py

from datetime import datetime
import os
import inspect

from Application.AppContext import ctx

# Default configuration
DEFAULT_CONFIG = {
    "cb_console_time": "Yes",
    "cb_console_colors": "Yes",
    "btn_console_info": True,
    "btn_console_warning": True,
    "btn_console_success": True,
    "btn_console_error": True,
    "btn_console_debug": True,
    "cb_file_enabled": "Yes",
    "btn_file_info": True,
    "btn_file_warning": True,
    "btn_file_success": True,
    "btn_file_error": True,
    "btn_file_debug": True,
    "sb_file_rotation": 10,
    "sb_file_retention": 7,
    "le_file_path": "./Logs",
    "cb_file_compression": "zip"
}

class Logger:

    # Logs dir
    LOG_PATH = "Logs/app.log"

    def __init__(self, config:dict) -> None:

        # Get c_levels and f_levels
        self.c_levels = {
            "INFO": config["btn_console_info"],
            "WARN": config["btn_console_warning"],
            "SUCCESS": config["btn_console_success"],
            "ERROR": config["btn_console_error"],
            "DEBUG": config["btn_console_debug"],
            "CRITICAL": True
        }

        if config["cb_file_enabled"] == "Yes":
            self.f_levels = {
                "INFO": config["btn_file_info"],
                "WARN": config["btn_file_warning"],
                "SUCCESS": config["btn_file_success"],
                "ERROR": config["btn_file_error"],
                "DEBUG": config["btn_file_debug"],
                "CRITICAL": True
            }
        else:
            self.f_levels = {
                "INFO": False,
                "WARN": False,
                "SUCCESS": False,
                "ERROR": False,
                "DEBUG": False,
                "CRITICAL": True
            }

        # Get time
        self.time = bool(config["cb_console_time"])

        # Log init
        self.info("Logger initialized")

    # Write to console and file methods for high efectivity
    def _cout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.c_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%H:%M:%S")

        # Create msg
        path = f"{filename}{":" if filename else ""}{func}{":" if func else ""}{row}"
        msg = f"{timestamp} {level:^10} {path}{" - " if path else ""}{msg}"
        print(msg)
    
    def _fout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.f_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create msg
        path = f"{filename}{":" if filename else ""}{func}{":" if func else ""}{row}"
        msg = f"{timestamp} {level:^10} {path}{" - " if path else ""}{msg}"
    
    # Info log
    def info(self, *args) -> None:
        self._cout("INFO", *args)
        self._fout("INFO", *args)

    # Warning log
    def warn(self, *args) -> None:
        self._cout("WARN", *args)
        self._fout("WARN", *args)

    # Success log
    def success(self, *args) -> None:
        self._cout("SUCCESS", *args)
        self._fout("SUCCESS", *args)

    # Error log
    def error(self, *args) -> None:
        # Get info about where was func calling

        # Filename, row and func
        caller_frame = inspect.stack()[1]

        filename = os.path.basename(caller_frame.filename)
        row = caller_frame.lineno
        func = caller_frame.function

        # Output
        self._cout("ERROR", *args, row=row, func=func, filename=filename)
        self._fout("ERROR", *args, row=row, func=func, filename=filename)

    # Debug log
    def debug(self, *args) -> None:
        # Get info about where was func calling

        # Filename, row and func
        caller_frame = inspect.stack()[1]

        filename = os.path.basename(caller_frame.filename)
        row = caller_frame.lineno
        func = caller_frame.function

        # Output
        self._cout("DEBUG", *args, row=row, func=func, filename=filename)
        self._fout("DEBUG", *args, row=row, func=func, filename=filename)

    # Critical -> Not in settings
    def critical(self, *args) -> None:
        # Get info about where was func calling

        # Filename, row and func
        caller_frame = inspect.stack()[1]

        filename = os.path.basename(caller_frame.filename)
        row = caller_frame.lineno
        func = caller_frame.function

        # Output
        self._cout("CRITICAL", *args, row=row, func=func, filename=filename)
        self._fout("CRITICAL", *args, row=row, func=func, filename=filename)

logger = Logger(ctx.config.get("LoggingPage", DEFAULT_CONFIG))

