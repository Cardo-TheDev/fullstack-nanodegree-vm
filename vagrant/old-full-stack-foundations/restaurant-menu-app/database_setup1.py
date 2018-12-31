''' sys module provides a number of variables and functions that can be used to 
manipulate different parts of python runtime enviroment '''
import sys
import os

# Comes in handy when writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# Used in the configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# Used for foriegn key relationship in mapper
from sqlalchemy.orm import relationship

# Used in configuration code
from sqlalchemy import create_engine

''' declarative_base lets sqla know our classes are special sqla classes
that corresponds to tables in our DB '''
Base = declarative_base()

# Classes which are object oriented representation of our data in python
class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(
        String(80), nullable = False)

    course = Column(String(250))

    description = Column(String(250))

    price = Column(String(8))

    restaurant_id = Column(
        Integer, ForeignKey('restaurant.id'))

    restaurant = relationship(Restaurant)


###### should be end of file #####
engine = create_engine(
    'sqlite:///restaurantmenu.db')

# goes into DB and adds the classes we create as new tables in our DB
Base.metadata.create_all(engine)