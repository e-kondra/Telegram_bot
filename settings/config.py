#  Configurations constants

import os
from emoji import emojize

# for remembering! buba_bot (bot's name )
# t.me/evilldead_bot (bot's username)
TOKEN = '5249069244:AAHlatQ05d12aWV9kD1YpFO3X_noS-YWcoM'

NAME_DB = 'products.db'

VERSION = '0.0.1'

AUTHOR = 'e-kondra'

#  path to Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#  path to DataBase (DB will be in directory 'settings')
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

#  control buttons
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Select product'),
    'INFO': emojize(':speech_balloon: ABOUT'),
    'SETTINGS': emojize('⚙️ TUNES'),
    'SEMIPRODUCT': emojize(':pizza: SEMIPRODUCT'),
    'GROCERY': emojize(':bread: GROCERY'),
    'ICE_CREAM': emojize(':shaved_ice: ICE_CREAM'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ Order'),
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