from sqlalchemy import Column, Boolean, Integer, String, Float, ForeignKey, DateTime
# model for tables relation
from sqlalchemy.orm import relationship, backref


from product import Products
from data_base.dbcore import Base


class Orders(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    date = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)
    products = relationship(Products,
                            backref=backref('orders',
                                            uselist=True,
                                            cascade='delete, all'))

    def __str__(self):
        return f'{self.quantity} {self.date}'

