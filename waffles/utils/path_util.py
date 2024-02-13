"""This module contains path utilities."""

from dataclasses import dataclass
from pathlib import Path

from settings import ENV


@dataclass
class Paths:
    """Paths class contains file paths used in the application."""
    _questions_dir = Path(f'data/questions/{ENV}')
    archived_txt = _questions_dir / 'archived.txt'
    delayed_txt = _questions_dir / 'delayed.txt'
    pending_txt = _questions_dir / 'pending.txt'

    _gifs_dir = Path('data/gifs')
    eating_txt = _gifs_dir / 'eating.txt'

    _logs_dir = Path('logs')
    waffles_log = _logs_dir / 'waffles.log'
