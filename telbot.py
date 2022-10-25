
from telebot import TeleBot  # from pyTelegramBotAPI

from settings import config
from handlers.handler_main import HandlerMain


class TelBot:
    #  The main class of telegram bot (server) with using pyTelegramBotAPI

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        # get token
        self.token = config.TOKEN
        # init Bot with token
        self.bot = TeleBot(self.token)
        # init events handler
        self.handler = HandlerMain(self.bot)

    def start(self):
        # Method for start bot's handler
        self.handler.handle()

    def run_bot(self):
        # Method launch main server's events
        print('run_bot')
        self.start()
        print('run_bot2')
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    t = ()
    print(type(t))
    bot = TelBot()
    bot.run_bot()