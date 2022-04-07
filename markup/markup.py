'''Form marking of interface elements'''

# special types of 'pyTelegramBotAPI' for elements of interface creation
from telebot.types import KeyboardButton

from data_base.dbalchemy import DBManager
from settings import config


class Keyboards:
    '''Class Keyboards forms marking of interface elements'''
    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        '''Create and return buttons emoji by parameters'''
        return  KeyboardButton(config.KEYBOARD[name])