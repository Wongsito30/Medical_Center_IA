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


def get_guardias():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/guardias")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/verGuardias/", response_model=List[page_schemas.Guardias])
async def show_Guardias(db:session=Depends(get_guardias)):
    guardias = db.query(page_models.Guardias).all()
    return guardias

@router.post("/registrarGuardias/", response_model=page_schemas.Guardias)
def create_Guardias(entrada: page_schemas.Guardias, db: session = Depends(get_guardias)):

    guardias = page_models.Guardias(nombre= entrada.nombre,matricula=entrada.matricula)
    
    db.add(guardias)
    db.commit()
    db.refresh(guardias)

    return guardias

@router.put("/cambiarGuardia/{guardia_id}",response_model=page_schemas.Guardias)
def mod_Guardia(guardia_id: int, entrada:page_schemas.Guardias,db:session=Depends(get_guardias)):
    guardia = db.query(page_models.Guardias).filter_by(id=guardia_id).first()
    guardia.nombre = entrada.nombre
    guardia.matricula = entrada.matricula
    db.commit()
    db.refresh(guardia)
    return guardia

@router.delete("/EliminarGuardia/{guardia_id}",response_model=page_schemas.respuesta)
def del_guardia(guardia_id: int,db:session=Depends(get_guardias)):
    guardia = db.query(page_models.Guardias).filter_by(id=guardia_id).first()
    db.delete(guardia)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta