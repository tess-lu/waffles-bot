"""This module contains utilities for the waffles bot."""

import traceback
import random
from pathlib import Path
from typing import Any, Callable
from functools import wraps

import requests

from settings import TOKEN, CHAT_ID
from utils.log_util import get_logger
from utils.path_util import Paths
from utils.enums import ContentType


logger = get_logger(logger_name=__name__, log_path=Paths.waffles_log)


def read_lines(path: str | Path) -> list[str]:
    """Return the lines from a text file."""
    lines = []
    for line in open(path, 'r', encoding='utf-8'):
        line = line.strip()
        if line:
            lines.append(line)
    return lines


def write_lines(path: str | Path, lines: list[str]) -> None:
    """Write lines to a text file."""
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(f'{line}\n')


def move_question(question: str,
                  *,
                  source_path: str | Path,
                  target_path: str | Path) -> None:
    """Move a question to another file."""
    source_questions = read_lines(source_path)
    target_questions = read_lines(target_path)
    source_questions.remove(question)
    target_questions.append(question)
    write_lines(source_path, source_questions)
    write_lines(target_path, target_questions)


def has_question_to_ask(*,
                        source_path: str | Path,
                        target_path: str | Path) -> bool:
    """Check if there are more questions to be asked."""
    source_questions = read_lines(source_path)
    target_questions = read_lines(target_path)
    if not source_questions:
        if (not source_questions and not target_questions) or \
           'delayed' in str(source_path):
            return False
        else:
            source_questions, target_questions = target_questions, source_questions
    write_lines(source_path, source_questions)
    write_lines(target_path, target_questions)
    return True


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


def ask_question(*, source_path: str | Path, target_path: str | Path) -> None:
    """Ask a question."""
    if has_question_to_ask(source_path=source_path, target_path=target_path):
        question_to_ask = read_lines(source_path)[0]
        waffles_send(question_to_ask)
        move_question(question_to_ask,
                      source_path=source_path,
                      target_path=target_path)
    else:
        waffles_send("I don't think we have more questions 🤔️")


def ask_pending_question() -> None:
    """Ask a pending question."""
    ask_question(source_path=Paths.pending_txt, target_path=Paths.archived_txt)


def ask_delayed_question() -> None:
    """Ask a delayed question."""
    ask_question(source_path=Paths.delayed_txt, target_path=Paths.archived_txt)


def delay_question() -> None:
    """Move the question to the delayed questions file."""
    archived_questions = read_lines(Paths.archived_txt)
    if archived_questions:
        question_to_delay = archived_questions[-1]
        move_question(question_to_delay,
                      source_path=Paths.archived_txt,
                      target_path=Paths.delayed_txt)
        waffles_send(f'Alright question "{question_to_delay}" is delayed!')
    else:
        waffles_send("I don't think there's anything to delay 🤔️")


def send_gif() -> None:
    """Send a gif."""
    eating_gifs = read_lines(Paths.eating_txt)
    gif_url = random.choice(eating_gifs)
    waffles_send(gif_url, content_type=ContentType.MEDIA)


def delete_question() -> None:
    """Delete a question from the file."""
    archived_questions = read_lines(Paths.archived_txt)
    if archived_questions:
        question_to_delete = archived_questions[-1]
        archived_questions.remove(question_to_delete)
        write_lines(Paths.archived_txt, archived_questions)
        waffles_send(f'Alright question "{question_to_delete}" is deleted!')
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
            else:
                pass  # no-op
        except Exception:
            error_message = traceback.format_exc()
            logger.critical(error_message)
            waffles_send(error_message)
            return None
    return wrapper
