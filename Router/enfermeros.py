from fastapi import APIRouter,HTTPException
from typing import List
from starlette.responses import RedirectResponse
from sqlalchemy.orm import session
from fastapi.params import Depends
from BD.Conn import engine, sessionlocal
import BD.schemas as page_schemas
import BD.Conn as page_conexion
import BD.models as page_models

page_models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_enfermeros():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/enfermeros")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verEnfermeros/", response_model=List[page_schemas.Enfermeros])
async def show_Enfermeros(db:session=Depends(get_enfermeros)):
    enfermeros = db.query(page_models.Enfermeros).all()
    return enfermeros

@router.post("/registrarEnfermeros/", response_model=page_schemas.Enfermeros)
def create_enfermeros(entrada: page_schemas.Enfermeros, db: session = Depends(get_enfermeros)):

    enfermeros = page_models.Enfermeros(nombre= entrada.nombre,matricula=entrada.matricula)
    
    db.add(enfermeros)
    db.commit()
    db.refresh(enfermeros)

    return enfermeros

@router.put("/cambiarEnfermero/{enfermo_id}",response_model=page_schemas.Enfermeros)
def mod_Enfermeros(enfermero_id: int, entrada:page_schemas.Enfermeros,db:session=Depends(get_enfermeros)):
    Enfermero = db.query(page_models.Enfermeros).filter_by(id=enfermero_id).first()
    Enfermero.nombre = entrada.nombre
    Enfermero.matricula = entrada.matricula
    db.commit()
    db.refresh(Enfermero)
    return Enfermero

@router.delete("/EliminarEnfermero/{enfermero_id}",response_model=page_schemas.respuesta)
def del_enfermero(enfermero_id: int,db:session=Depends(get_enfermeros)):
    enfermero = db.query(page_models.Enfermeros).filter_by(id=enfermero_id).first()
    db.delete(enfermero)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta