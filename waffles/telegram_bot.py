"""The Telegram bot service."""

from xmlrpc.client import ServerProxy

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

from settings import TOKEN
from utils.enums import QuestionStatus
from utils.waffles_util import (handle_exceptions, waffles_send,
                                ask_question, delay_question, delete_question)


supervisor = ServerProxy('http://127.0.0.1:9001/RPC2').supervisor


@handle_exceptions
def wake_up(update: Update, context: CallbackContext) -> None:
    """Start qotd service."""
    qotd_state = supervisor.getProcessInfo('qotd')['statename']
    if qotd_state == 'RUNNING':
        reply = "I'm already up 😜"
    else:
        supervisor.startProcess('qotd')
        reply = "Hey chat, I'm up! 😁"
    waffles_send(reply)


@handle_exceptions
def sleep(update: Update, context: CallbackContext) -> None:
    """Stop qotd service."""
    qotd_state = supervisor.getProcessInfo('qotd')['statename']
    if qotd_state == 'STOPPED':
        reply = '😴'
    else:
        supervisor.stopProcess('qotd')
        reply = 'Going to sleep now, good night chat 🤗'
    waffles_send(reply)


@handle_exceptions
def next_pending(update: Update, context: CallbackContext) -> None:
    """Ask the next pending question."""
    ask_question(QuestionStatus.PENDING)


@handle_exceptions
def next_delayed(update: Update, context: CallbackContext) -> None:
    """Ask the next delayed question."""
    ask_question(QuestionStatus.DELAYED)


@handle_exceptions
def delay(update: Update, context: CallbackContext) -> None:
    """Delay a question."""
    delay_question()


@handle_exceptions
def delay_and_next(update: Update, context: CallbackContext) -> None:
    """Delay a question and ask the next pending question."""
    delay_question()
    ask_question(QuestionStatus.PENDING)


@handle_exceptions
def delete(update: Update, context: CallbackContext) -> None:
    """Delete a question."""
    delete_question()


@handle_exceptions
def delete_and_next(update: Update, context: CallbackContext) -> None:
    """Delete a question and ask the next pending question."""
    delete_question()
    ask_question(QuestionStatus.PENDING)


def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('wake_up', wake_up))
    dp.add_handler(CommandHandler('sleep', sleep))
    dp.add_handler(CommandHandler('next_pending', next_pending))
    dp.add_handler(CommandHandler('next_delayed', next_delayed))
    dp.add_handler(CommandHandler('delay', delay))
    dp.add_handler(CommandHandler('delay_and_next', delay_and_next))
    dp.add_handler(CommandHandler('delete', delete))
    dp.add_handler(CommandHandler('delete_and_next', delete_and_next))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
