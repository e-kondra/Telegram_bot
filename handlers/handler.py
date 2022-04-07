'''Base class Handler'''

# for Abstract classes realization import abc
import abc
# import keyboards and key's marking
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):

        self.bot = bot

        self.keybords = Keyboards()
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass