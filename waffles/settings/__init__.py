"""This module contains configuration variables."""

import os
from decouple import config


ENV = os.getenv('ENV')

TOKEN = config('TOKEN')
CHAT_ID = config('CHAT_ID', cast=int)

FROM_VALUE = config('FROM_VALUE', cast=int, default=3600)
TO_VALUE = config('TO_VALUE', cast=int, default=36000)
