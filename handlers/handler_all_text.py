from handlers.handler import Handler
from settings import config
from settings.message import MESSAGES


class HandlerAllText(Handler):
    """
    Class which handle input text messages from pressing buttons
    """

    def __init__(self, bot):
        super().__init__(bot)
        # orders step
        self.step = 0

    def press_btn_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode='HTML',
                              reply_markup=self.keybords.info_menu())

    def press_btn_settings(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode='HTML',
                              reply_markup=self.keybords.settings_menu())

    def press_btn_back(self, message):
        self.bot.send_message(message.chat.id, "You're back", reply_markup=self.keybords.start_menu())

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == config.KEYBOARD['INFO']:
                self.press_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.press_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.press_btn_back(message)

