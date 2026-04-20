# Logger.py

# Importing system modules
from loguru import logger # type: ignore
import sys
import os

# Main class Logger
class Logger:

    # Logs dir
    logsDir = "Logs"

    # Initiator
    def __init__(self, config, serviceName) -> None:
        
        # Remove default config
        logger.remove()

        # Service name
        self.serviceName = serviceName
        

        # Console format
        console_format = ""

        # Time if is allowed
        if config.get("cb_console_time") == "Yes":
            console_format += "<yellow>{time:YYYY-MM-DD}</yellow> <white>{time:HH:mm:ss.SSS}</white> "

        # Changing level color
        console_format += "<level><b>{level: ^8}</b></level> "

        # Service name
        console_format += f"<cyan>[{serviceName: ^12}]</cyan> "

        # Single messgae
        console_format += "<level> <normal>{message}</normal></level>"
        # Format for console

        # Filtring levels
        console_levels = set()
        if config.get("btn_console_info"): console_levels.add("INFO")
        if config.get("btn_console_error"): console_levels.add("ERROR")
        if config.get("btn_console_debug"): console_levels.add("DEBUG")
        if config.get("btn_console_warning"): console_levels.add("WARNING")
        if config.get("btn_console_success"): console_levels.add("SUCCESS")

        # Console handler
        logger.add(
            sys.stderr,
            level="TRACE",
            filter=lambda r: r["level"].name in console_levels,
            format=console_format,
            colorize=True if config.get("cb_console_colors") == "Yes" else False
        )

        # If file logging is allowed
        if config.get("cb_file_enabled") == "Yes":
            # File log if there is any
            log_dir = config.get("le_file_path") if config.get("le_file_path") else "Logs"
            log_file = os.path.join(log_dir, "app.log")

            # Filtr all levels by settings
            file_levels = set()
            if config.get("btn_file_info"): file_levels.add("INFO")
            if config.get("btn_file_error"): file_levels.add("ERROR")
            if config.get("btn_file_debug"): file_levels.add("DEBUG")
            if config.get("btn_file_warning"): file_levels.add("WARNING")
            if config.get("btn_file_success"): file_levels.add("SUCCESS")

            # If compression
            compression = config.get("cb_file_compression")
            if compression == "None": compression = None

            # Add file hadnling 
            logger.add(
                log_file,
                level="TRACE",
                # Format more detailed
                format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
                filter=lambda r: r["level"].name in file_levels,
                rotation=f"{config.get('sb_file_rotation', 10)} MB",
                retention=f"{config.get('sb_file_retention', 7)} days",
                compression=compression,
                backtrace=True,
                diagnose=True
            )

        # First logger message
        logger.info(f"Logger initialized for {serviceName}")
    
    # Update settings
    def updateConfig(self, newConfig) -> None:
        # Import loguru again
        from loguru import logger # type: ignore

        # Remove configuration
        logger.remove() 
        
        # Run constructor again with new config
        self.__init__(newConfig, self.serviceName)

        # Log successfully update
        logger.success("Logger configuration updated successfully.")

    # Clearing logs
    @classmethod
    def clear_logs(cls) -> None:
        # Open file
        with open(f"{cls.logsDir}/app.log", "w") as log:
            None
