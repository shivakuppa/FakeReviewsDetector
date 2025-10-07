import logging
import logging.config
import os
from datetime import datetime

# Timestamped log filenames
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
ERROR_LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}-ERROR.log"

# Base logs directory (same level as src)
BASE_LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

# Separate subdirectories for standard and error logs
STANDARD_LOG_DIR = os.path.join(BASE_LOG_DIR, "standard")
ERROR_LOG_DIR = os.path.join(BASE_LOG_DIR, "error")

# Ensure directories exist
os.makedirs(STANDARD_LOG_DIR, exist_ok=True)
os.makedirs(ERROR_LOG_DIR, exist_ok=True)

# Full paths to log files
LOG_FILE_PATH = os.path.join(STANDARD_LOG_DIR, LOG_FILE)
ERROR_LOG_FILE_PATH = os.path.join(ERROR_LOG_DIR, ERROR_LOG_FILE)

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
            "maxBytes": 1000000,
            "backupCount": 5,
            "encoding": "utf8"
        },
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "error_file_handler": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "standard",
            "filename": ERROR_LOG_FILE_PATH,
            "encoding": "utf8"
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file_handler", "error_file_handler"]
    },
}

# Apply configuration
logging.config.dictConfig(logging_config)

# Optional: module-level logger
logger = logging.getLogger(__name__)
