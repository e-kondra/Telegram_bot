from handlers.handler_com import HandlerCommands
from handlers.handler_all_text import HandlerAllText


class HandlerMain:
    # Class for merge and run all handlers
    def __init__(self, bot):
        #  handlers init
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)

    def handle(self):
        #  handlers run
        self.handler_commands.handle()
        self.handler_all_text.handle()

