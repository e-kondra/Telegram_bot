# Input commands handling
from handlers.handler import Handler


class HandlerCommands(Handler):
    # Class - input commands handler

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        # handle /start command
        self.bot.send_message(message.chat.id,
                              f'Hello! Await further tasks',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # handle of start command
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
