from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Medicos(BaseModel):
    id: int
    nombre: str
    matricula: str
    
    class Config:
        from_atributtes = True

class Enfermeros(BaseModel):
    id: int
    nombre: str
    matricula: str
    
    class Config:
        from_atributtes = True

class Guardias(BaseModel):
    id: int
    nombre: str

    
    class Config:
        from_atributtes = True


class respuesta(BaseModel):
     mensaje: str