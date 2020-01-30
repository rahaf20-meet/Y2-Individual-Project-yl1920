from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class North(Base):
	__tablename__ = "north"
	Id = Column(Integer, primary_key=True)
	locationName = Column(String)
	locationInfo = Column(String)
	pictureLink = Column(String)
	top = Column(Float)
	left = Column(Float)
	# def __repr__(self):
	# 	return str([self.locationName, self.locationInfo, self.pictureLink, self.top,self.left])

class South(Base):
	__tablename__ = "south"
	Id = Column(Integer, primary_key=True)
	top = Column(Float)
	left = Column(Float)
	locationName = Column(String)
	locationInfo = Column(String)
	pictureLink = Column(String)

class East(Base):
	__tablename__ = "east"
	Id = Column(Integer, primary_key=True)
	top = Column(Float)
	left = Column(Float)
	locationName = Column(String)
	locationInfo = Column(String)
	pictureLink = Column(String)

class West(Base):
	__tablename__ = "west"
	Id = Column(Integer, primary_key=True)
	top = Column(Float)
	left = Column(Float)
	locationName = Column(String)
	locationInfo = Column(String)
	pictureLink = Column(String)

class Information(Base):
	__tablename__ = "info"
	Id = Column(Integer, primary_key=True)
	locationName = Column(String)
	locationInfo = Column(String)
	pictureLink = Column(String)
	compass = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


	
# class Cart(Base):
# 	__tablename__="productID"
# 	Id = Column(Integer, primary_key=True)
# 	productID = Column(Integer)