"""This module contains log utilities."""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(*,
               logger_name: str,
               log_path: str | Path,
               max_mb: int = 10,
               max_backup: int = 1) -> logging.Logger:
    """Init logger."""
    fmt = '%(asctime)s - %(pathname)s:%(lineno)d - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(log_path,
                                       encoding='utf-8',
                                       maxBytes=10**6*max_mb,
                                       backupCount=max_backup)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
