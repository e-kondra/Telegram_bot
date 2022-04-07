from sqlalchemy import  Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from models.category import Category
from models.product import Products
from models.service import Services


Base = declarative_base()

class Actions(Base):

    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_begin = Column(DateTime)
    date_end = Column(DateTime)
    discount = Column(Float)
    category_id = Column(Integer, ForeignKey('category.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    category = relationship(Category,
                            backref=backref('actions',  # current table
                                                      uselist=True,  # for all relations
                                                      cascade='delete, all'))
    products = relationship(Products,
                            backref=backref('actions',
                                            uselist=True,
                                            cascade='delete, all'))
    services = relationship(Services,
                            backref=backref('actions',
                                            uselist=True,
                                            cascade='delete, all'))

    def __str__(self):
        return f'{self.name}'