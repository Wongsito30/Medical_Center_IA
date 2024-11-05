from sqlalchemy import Column, Integer, String, LargeBinary, Float, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Medicos(Base):
    __tablename__ = 'medicos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    Matricula = Column(String(20)) 

class Enfermeros(Base):
    __tablename__ = 'enfermeros'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    Matricula = Column(String(20)) 

class Guardias(Base):
    __tablename__ = 'guardias'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))