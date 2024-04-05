"""This module contains utilities for the waffles bot."""

import traceback
from typing import Any, Callable
from functools import wraps

import requests

from settings import TOKEN, CHAT_ID
from utils.log_util import get_logger
from utils.path_util import Paths
from utils.enums import QuestionStatus, ContentType
from utils.db_util import (get_question, update_question_status,
                           get_most_recently_archived_question,
                           pick_random_gif)


logger = get_logger(logger_name=__name__, log_path=Paths.waffles_log)


def waffles_send(content: Any,
                 *,
                 content_type: ContentType = ContentType.TEXT) -> None:
    """Send a message to the Telegram chat."""
    if content_type == ContentType.TEXT:
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={content}'
    elif content_type == ContentType.MEDIA:
        url = f'https://api.telegram.org/bot{TOKEN}/sendVideo?chat_id={CHAT_ID}&video={content}'
    logger.info(f'Sending content: {url}')
    response = requests.get(url, timeout=30)
    logger.info(f'Response: {response.json()}')


def ask_question(status: str) -> None:
    """Ask a question with the given status."""
    question = get_question(status)
    if question:
        waffles_send(question.text)
        update_question_status(question_id=question.id,
                               new_status=QuestionStatus.ARCHIVED)
    else:
        waffles_send("I don't think we have more questions 🤔️")


def send_gif() -> None:
    """Send a gif."""
    gif_url = pick_random_gif()
    waffles_send(gif_url, content_type=ContentType.MEDIA)


def delay_question() -> None:
    """Delay a question."""
    question = get_most_recently_archived_question()
    if question:
        update_question_status(question_id=question.id,
                               new_status=QuestionStatus.DELAYED)
        waffles_send(f'Alright question "{question.text}" is delayed!')
    else:
        waffles_send("I don't think there's anything to delay 🤔️")


def delete_question() -> None:
    """Delete a question."""
    question = get_most_recently_archived_question()
    if question:
        update_question_status(question_id=question.id,
                               new_status=QuestionStatus.DELETED)
        waffles_send(f'Alright question "{question.text}" is deleted!')
        send_gif()
    else:
        waffles_send("I don't think there's anything to delete 🤔️")


def handle_exceptions(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to handle exceptions gracefully and
    send the error message to the Telegram chat.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            update = args[0]
            chat_id = update.message.chat_id
            logger.info(f'{chat_id=}')
            if chat_id == CHAT_ID:
                result = func(*args, **kwargs)
                return result
        except Exception:
            error_message = traceback.format_exc()
            logger.critical(error_message)
            waffles_send(error_message)
            return None
    return wrapper
