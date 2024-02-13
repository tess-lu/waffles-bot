"""This module contains custom Enum classes."""

from enum import StrEnum


class Mode(StrEnum):
    """Enumeration representing different environments."""
    DEV = 'dev'
    PROD = 'prod'


class ContentType(StrEnum):
    """Enumeration representing different content types."""
    TEXT = 'text'
    MEDIA = 'media'
