"""This module contains configuration variables."""

import os
from decouple import config


ENV = os.getenv('ENV')

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/waffles_{ENV}'

TOKEN = config('TOKEN')
CHAT_ID = config('CHAT_ID', cast=int)

FROM_VALUE = config('FROM_VALUE', cast=int, default=3600)
TO_VALUE = config('TO_VALUE', cast=int, default=36000)
