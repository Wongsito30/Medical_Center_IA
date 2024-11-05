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


def get_medicos():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/medicos")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verMedicos/", response_model=List[page_schemas.Medicos])
async def show_Medicos(db:session=Depends(get_medicos)):
    medicos = db.query(page_models.Medicos).all()
    return medicos

@router.post("/registrarMedicos/", response_model=page_schemas.Medicos)
def create_medicos(entrada: page_schemas.Medicos, db: session = Depends(get_medicos)):

    medicos = page_models.Medicos(nombre= entrada.nombre,matricula=entrada.matricula)
    
    db.add(medicos)
    db.commit()
    db.refresh(medicos)

    return medicos

@router.put("/cambiarMedicos/{medico_id}",response_model=page_schemas.Medicos)
def mod_medicos(medico_id: int, entrada:page_schemas.Medicos,db:session=Depends(get_medicos)):
    Medicos = db.query(page_models.Medicos).filter_by(id=medico_id).first()
    Medicos.nombre = entrada.nombre
    Medicos.matricula = entrada.matricula
    db.commit()
    db.refresh(Medicos)
    return Medicos

@router.delete("/Eliminar/{medico_id}",response_model=page_schemas.respuesta)
def del_medico(medico_id: int,db:session=Depends(get_medicos)):
    medico = db.query(page_models.Medicos).filter_by(id=medico_id).first()
    db.delete(medico)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta