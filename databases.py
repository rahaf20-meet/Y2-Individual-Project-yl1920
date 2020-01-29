from model import Base, North, South, East, West, User
from flask import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def createSession():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session 

def add_user(username,password):
	session = createSession()
	user = User(username=username, password=password)
	session.add(user)
	session.commit()

def query_by_user(username,password):
	session = createSession()
	user = session.query(
		User).filter_by(
		username=username).first()
	if user in session: 
		if password == user.password:
			return user
		else: 
			return None
	return user

def addNorth(top,left,locationName,locationInfo,pictureLink):
	session = createSession()
	north_object = North (
		top=top,
		left=left,
		locationName=locationName,
		locationInfo=locationInfo,
		pictureLink=pictureLink),
	session.add(north_object)
	session.commit()
	session.close()

def addSouth(top,left,locationName,locationInfo,pictureLink):
	session = createSession()
	south_object = South (
		top=top,
		left=left,
		locationName=locationName,
		locationInfo=locationInfo,
		pictureLink=pictureLink)
	session.add(south_object)
	session.commit()
	session.close()

def addEast(top,left,locationName,locationInfo,pictureLink):
	session = createSession()
	east_object = East (
		top=top,
		left=left,
		locationName=locationName,
		locationInfo=locationInfo,
		pictureLink=pictureLink)
	session.add(east_object)
	session.commit()
	session.close()

def addWest(top,left,locationName,locationInfo,pictureLink):
	session = createSession()
	west_object = West (
		top=top,
		left=left,
		locationName=locationName,
		locationInfo=locationInfo,
		pictureLink=pictureLink)
	session.add(west_object)
	session.commit()
	session.close()

def query_all_north():
	session = createSession()
	north = session.query(
      North).all()
	session.close()
	return north

def query_all_south():
	session = createSession()
	south = session.query(
      South).all()
	session.close()
	return south

def query_all_east():
	session = createSession()
	east = session.query(
      East).all()
	session.close()
	return east

def query_all_west():
	session = createSession()
	west = session.query(
      West).all()
	session.close()
	return west


# def editLocation(Id): #by id
# 	session = createSession()
# 	location_object = session.query(
#        Location).filter_by(
#        Id=Id).first()
# 	location_object.pos_x = pos_x
# 	product_object.pos_y = pos_y
# 	session.commit()
# 	session.close()

# def deleteLocation(locationName):
# 	session = createSession()
# 	session.query(Location).filter_by(
#        locationName=locationName).delete()
# 	session.commit()
# 	session.close()

# def addInfo(locationName, locationInfo, pictureLink):
# 	session = createSession()
# 	info_object = Information (
# 		locationName=locationName ,
# 		locationInfo=locationInfo ,
# 		pictureLink=pictureLink)
# 	session.add(info_object)
# 	session.commit()
# 	session.close()


# def editProduct(Id, name): #by id
# 	session = createSession()
# 	north_object = session.query(
#        North).filter_by(
#        Id=Id).first()
# 	location_object.locationInfo = locationInfo
# 	product_object.pictureLink = pictureLink
# 	session.commit()
# 	session.close()

# def deleteProduct(id):
# 	session = createSession()
# 	session.query(North).filter_by(
#        id=id).delete()
# 	session.commit()
# 	session.close()


# def add_to_cart(productID):

