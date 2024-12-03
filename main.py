from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Router import sensorHuella 
from Router import sensorNFC
from Router import sensorRostro

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensorHuella.router, tags=["Sensor Huella"])
app.include_router(sensorNFC.router, tags=["Sensor NFC"])
app.include_router(sensorRostro.router, tags=["Sensor Rostro"])


@app.get("/")
async def root():
    return {"message": "Hello World"}