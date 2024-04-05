"""This module contains path utilities."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Paths:
    """File paths used in the application."""
    _logs_dir = Path('logs')
    waffles_log = _logs_dir / 'waffles.log'
