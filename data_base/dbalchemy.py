from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from settings import config
from models.product import Products


class Singletone(type):
    '''
    Pattern, creating only one object of class
    and giving global access point to it
    '''
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singletone):
    """
    Class - manager for work with Data Base
    """

    def __init__(self):
        # init session and switch ob DB
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_products_category(self, category):
        # return all products by category
        result = self._session.query(Products).filter_by(category_id=category).all()
        self.close()
        return result

    def close(self):
        self._session.close()