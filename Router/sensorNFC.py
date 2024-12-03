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


def get_NFC():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/NFC")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verNFC/", response_model=List[page_schemas.sensorNFC])
async def show_NFC(db:session=Depends(get_NFC)):
    sNFC = db.query(page_models.NFC).all()
    return sNFC

@router.post("/registrarNFC/", response_model=page_schemas.sensorNFC)
def create_NFC(entrada: page_schemas.sensorNFC, db: session = Depends(get_NFC)):

    sNFC = page_models.sensorNFC(nombre= entrada.nombre,puesto=entrada.puesto,uid=entrada.uid, fecha=entrada.fecha)
    
    db.add(sNFC)
    db.commit()
    db.refresh(sNFC)

    return sNFC

@router.put("/cambiarNFC/{nfc_id}",response_model=page_schemas.sensorNFC)
def mod_NFC(NFC_id: int, entrada:page_schemas.sensorNFC,db:session=Depends(get_NFC)):
    sNFC = db.query(page_models.sensorNFC).filter_by(id=NFC_id).first()
    sNFC.nombre = entrada.nombre
    sNFC.puesto = entrada.puesto
    sNFC.uid=entrada.uid 
    sNFC.fecha=entrada.fecha
    db.commit()
    db.refresh(sNFC)
    return sNFC

@router.delete("/EliminarNFC/{nfc_id}",response_model=page_schemas.respuesta)
def del_nfc(nfc_id: int,db:session=Depends(get_NFC)):
    sNFC = db.query(page_models.sensorNFC).filter_by(id=nfc_id).first()
    db.delete(sNFC)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta