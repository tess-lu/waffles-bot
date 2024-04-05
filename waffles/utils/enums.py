"""This module contains custom Enum classes."""

from enum import StrEnum


class Environment(StrEnum):
    """Enumeration representing different environments."""
    DEV = 'dev'
    PROD = 'prod'


class QuestionStatus(StrEnum):
    """Enumeration representing the status of a question."""
    PENDING = 'pending'
    ARCHIVED = 'archived'
    DELAYED = 'delayed'
    DELETED = 'deleted'


class ContentType(StrEnum):
    """Enumeration representing different content types."""
    TEXT = 'text'
    MEDIA = 'media'
