from sqlalchemy import  Column, Boolean, Integer, String, Float, ForeignKey
# model for tables relation
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from category import Category


Base = declarative_base()

class Services(Base):

    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # for cascade deleting data from table
    category = relationship(Category, backref=backref('services',  # current table
                                                      uselist=True,  # for all relations
                                                      cascade='delete, all'))

    def __str__(self):
        return f'{self.name} {self.price}'