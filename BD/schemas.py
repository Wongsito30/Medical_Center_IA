from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

class sensorRostro(BaseModel):
    id: int
    nombre: str
    puesto: str
    
    class Config:
        from_atributtes = True

class sensorNFC(BaseModel):
    id: int
    nombre: str
    puesto: str
    uid: str
    fecha: datetime
    
    class Config:
        from_atributtes = True

class sensorHuella(BaseModel):
    id: int
    nombre: str
    puesto: str

    
    class Config:
        from_atributtes = True


class respuesta(BaseModel):
     mensaje: str