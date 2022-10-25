from datetime import datetime
from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_base.dbcore import Base

from settings import config, utility
from models.product import Products
from models.order import Orders


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

    def select_all_products_id(self):
        """ :return all products id in order"""
        result = self._session.query(Orders.product_id).all()
        self.close()
        return utility._convert(result)

    def select_order_quantity(self, product_id):
        """:return product quantity in order """
        result = self._session.query(Orders.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def update_order_value(self, product_id, name, value):
        """Renew orders data by product_id"""
        self._session.query(Orders).filter_by(
            product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_quantity(self, rownum):
        result = self._session.query(
            Products.quantity).filter_by(id=rownum).one()
        self.close()
        return result.quantity

    def update_product_value(self, rownum, name, value):
        """Renew product quantity in storage by products num (rownum)"""
        self._session.query(Products).filter_by(id=rownum).update({name: value})
        self._session.commit()
        self.close()

    def _add_orders(self, quantity, product_id, user_id):
        # Fill order
        # get all products id as list from order
        all_id_product = self.select_all_products_id()
        if product_id in all_id_product:  # where is a product in order
            # renew tables products and orders
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)

            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
            return
        else:  # new product in order
            order = Orders(quantity=quantity,
                           product_id=product_id,
                           user_id=user_id,
                           date=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

        self._session.add(order)
        self._session.commit()
        self.close()

    def select_single_product_name(self, num):
        """ return product name by product id"""
        result = self._session.query(Products.name).filter_by(id=num).one()
        self.close()
        return result.name

    def select_single_product_title(self, num):
        """return product title by product id"""
        result = self._session.query(Products.title).filter_by(id=num).one()
        self.close()
        return result.title

    def select_single_product_price(self, num):
        """return product price by product id"""
        result = self._session.query(Products.price).filter_by(id=num).one()
        self.close()
        return result.price


