import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    character_fav = relationship("Character_fav", foreign_keys ="[Character_fav.user_id]")
    planet_fav = relationship("Planet_fav", foreign_keys="[Planet_fav.user_id]")
    nave_fav = relationship("nave_fav", foreign_keys="[Nave_fav.user_id]")


class Character(Base):
    __tablename__ = "Character"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    character_fav = relationship("Character_fav", foreign_keys="[Character_fav.character_id]")

class Planet(Base):
    __tablename__ = "Planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    planet_fav = relationship("Planet_fav", foreign_keys="[Planet_fav.planet_id]")


class Nave(Base):
    __tablename__ = "Nave"
    id = Column(Integer, primary_key=True)
    name = Column(String( 250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    nave_fav = relationship("Nave_fav", foreign_keys="[Nave_fav.nave_id]")

class Character_fav(Base):
    __tablename__ = "Character_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    character_id = Column(Integer, ForeignKey("Character.id"))
    user = relationship("User", foreign_keys=[user_id])
    character = relationship ("Character", foreign_keys=[character_id])

class Planet_fav(Base):
    __tablename__ = "Planet_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    planet_id = Column(Integer, ForeignKey("Planet.id"))
    user = relationship("User", foreign_keys=[user_id])
    planet = relationship("Planet", foreign_keys=[planet_id])


class Nave_fav(Base):
    __tablename__ = "Nave_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ("User.id"))
    nave_id = Column(Integer, ForeignKey("Nave.id"))
    user = relationship("User", foreign_keys=[user_id])
    nave = relationship("Nave", foreign_keys=[nave_id])


# Generar el diagrama de ER
render_er(Base, "diagram.png")
