from sqlalchemy import Column, String, Boolean, Integer
# class - constructor for working with declarative style
from sqlalchemy.ext.declarative import declarative_base
# init declarative style
Base = declarative_base()


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __str__(self):
        return self.name
