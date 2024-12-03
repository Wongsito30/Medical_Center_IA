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


def get_rostro():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/rostro")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verRostro/", response_model=List[page_schemas.sensorRostro])
async def show_Rostro(db:session=Depends(get_rostro)):
    rostro = db.query(page_models.sensorRostro).all()
    return rostro

@router.post("/registrarRostro/", response_model=page_schemas.sensorRostro)
def create_Rostro(entrada: page_schemas.sensorRostro, db: session = Depends(get_rostro)):

    Rostro = page_models.sensorRostro(nombre= entrada.nombre,puesto=entrada.puesto )
    
    db.add(Rostro)
    db.commit()
    db.refresh(Rostro)

    return Rostro

@router.put("/cambiarRostro/{rostro_id}",response_model=page_schemas.sensorRostro)
def mod_rostro(rostro_id: int, entrada:page_schemas.sensorRostro,db:session=Depends(get_rostro)):
    Rostro = db.query(page_models.sensorRostro).filter_by(id=rostro_id).first()
    Rostro.nombre = entrada.nombre
    Rostro.puesto = entrada.puesto
    db.commit()
    db.refresh(Rostro)
    return Rostro

@router.delete("/Eliminar/{rostro_id}",response_model=page_schemas.respuesta)
def del_rostro(rostro_id: int,db:session=Depends(get_rostro)):
    Rostro = db.query(page_models.sensorRostro).filter_by(id=rostro_id).first()
    db.delete(Rostro)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta