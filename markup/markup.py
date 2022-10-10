'''Form marking of interface elements'''

# special types of 'pyTelegramBotAPI' for elements of interface creation
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from data_base.dbalchemy import DBManager
from settings import config


class Keyboards:
    #  Class Keyboards forms marking of interface elements
    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        #  Create and return buttons emoji object by parameters(button's name)
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Create buttons markup in the main menu and return markup's object
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # buttons markup in the menu
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def settings_menu(self):
        # create markup in the Settings menu
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def info_menu(self):
        # create markup in the Info menu
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def category_menu(self):
        """
        create new markup in category menu
        :return: markup
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    def remove_menu(self):
        # remove menu
        return ReplyKeyboardRemove()
