from sqlalchemy import  Column, Boolean, Integer, String, Float, ForeignKey
# model for tables relation
from sqlalchemy.orm import relationship, backref

from models.category import Category
from data_base.dbcore import Base


class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # for cascade deleting data from table
    category = relationship(Category, backref=backref('products', # current table
                                                      uselist=True, # for all relations
                                                      cascade='delete, all'))

    def __str__(self):
        return f'{self.name} {self.title} {self.price}'