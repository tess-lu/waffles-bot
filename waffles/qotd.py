"""The qotd (question of the day) service."""

import time

import schedule

from settings import FROM_VALUE, TO_VALUE
from utils.waffles_util import ask_pending_question


def main() -> None:
    schedule.every(FROM_VALUE).to(TO_VALUE).seconds.do(ask_pending_question)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
