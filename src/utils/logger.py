import logging
import logging.config
import os
from datetime import datetime
from pathlib import Path

# Root directory (two levels up from current file)
ROOT_DIR = Path(__file__).resolve().parents[2]
LOGS_DIR = ROOT_DIR / "logs"
STANDARD_LOG_DIR = LOGS_DIR / "standard"
ERROR_LOG_DIR = LOGS_DIR / "error"

STANDARD_LOG_DIR.mkdir(parents=True, exist_ok=True)
ERROR_LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = STANDARD_LOG_DIR / f"{datetime.now():%m_%d_%Y_%H_%M_%S}.log"
ERROR_LOG_FILE_PATH = ERROR_LOG_DIR / f"{datetime.now():%m_%d_%Y_%H_%M_%S}-ERROR.log"


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
