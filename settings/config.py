#  Configurations constants

import os
from emoji import emojize

# for remembering! buba_bot (bot's name )
# t.me/evilldead_bot (bot's username)
TOKEN = '5249069244:AAHlatQ05d12aWV9kD1YpFO3X_noS-YWcoM'

NAME_DB = 'products.sqlite'

VERSION = '0.0.1'

AUTHOR = 'e-kondra'

#  path to Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#  path to DataBase (DB will be in directory 'settings')
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

#  control buttons
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

COMMANDS = {
    'START': 'start',
    'HELP': 'help',
}