from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Hotel(Base):
    __tablename__="hotels"
    
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    location=Column(String)
    
    rooms=relationship("Room", back_populates="hotel")
    

class Rooms(Base):
    __tablename__="rooms"
    
    id=Column(Integer, primary_key=True, index=True)
    number=Column(String, index=True)
    available=Column(Boolean, default=True)
    hotel_id=Column(Integer, ForeignKey("hotels.id"))
    
    hotel=relationship("Hotel", back_populates="rooms")