from sqlalchemy import Column, Integer, String, BINARY, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class sensorRostro(Base):
    __tablename__ = 'sensorRostros'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    puesto = Column(String(20)) 

class sensorNFC(Base):
    __tablename__ = 'sensorNFC'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    puesto = Column(String(20)) 
    uid = Column(BINARY(8))
    fecha = Column(DateTime)

class sensorHuella(Base):
    __tablename__ = 'sensorHuellas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    puesto = Column(String(20)) 