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


def get_huella():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/huellas")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verHuellas/", response_model=List[page_schemas.sensorHuella])
async def show_huella(db:session=Depends(get_huella)):
    huellas = db.query(page_models.sensorHuella).all()
    return huellas

@router.post("/registrarHuellas/", response_model=page_schemas.sensorHuella)
def create_huella(entrada: page_schemas.sensorHuella, db: session = Depends(get_huella)):

    huella = page_models.sensorHuella(nombre= entrada.nombre,puesto=entrada.puesto)
    
    db.add(huella)
    db.commit()
    db.refresh(huella)

    return huella

@router.put("/cambiarHuellas/{huella_id}",response_model=page_schemas.sensorHuella)
def mod_Huella(huella_id: int, entrada:page_schemas.sensorHuella,db:session=Depends(get_huella)):
    huella = db.query(page_models.sensorHuella).filter_by(id=huella_id).first()
    huella.nombre = entrada.nombre
    huella.puesto = entrada.puesto
    db.commit()
    db.refresh(huella)
    return huella

@router.delete("/eliminarHuella/{huella_id}",response_model=page_schemas.respuesta)
def del_huella(huella_id: int,db:session=Depends(get_huella)):
    huella = db.query(page_models.sensorHuella).filter_by(id=huella_id).first()
    db.delete(huella)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta