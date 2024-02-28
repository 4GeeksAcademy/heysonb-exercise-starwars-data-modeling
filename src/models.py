import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    registered = Column(DateTime, nullable=False)
    Favorites_planets_id = Column(Integer, ForeignKey('favorites.id'))
    Favorites_planets = relationship('Favorites')
    Favorites_characters_id = Column(Integer, ForeignKey('favorites.id'))
    Favorites_characters = relationship('Favorites')

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(DateTime, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homewrodl = relationship('Planets')
   


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    terrain = Column(String(250))
    residents_id = Column(Integer, ForeignKey('characters.id'))
    residents = relationship('Characters')
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)

    

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)    

    

 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
