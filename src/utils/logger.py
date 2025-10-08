import logging
import logging.config
import os
from datetime import datetime

# Root directory (two levels up from current file)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Log directories
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# Create directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# Log file paths
LOG_FILE_PATH = os.path.join(LOGS_DIR, "app.log")   # fixed name for rotation

# Logging configuration dictionary
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": LOG_FILE_PATH,
            "maxBytes": 1_000_000,
            "backupCount": 10,
            "encoding": "utf8"
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file_handler"]
    },
}

# Apply configuration
logging.config.dictConfig(logging_config)

# Module-level logger
logger = logging.getLogger(__name__)

# Add a spacer/header at the start of each execution
header = "\n" + "="*60 + f"\nNEW EXECUTION STARTED: {datetime.now():%Y-%m-%d %H:%M:%S}\n" + "="*60 + "\n"
logger.info(header)
