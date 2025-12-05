from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud, schemas

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/jugadores", response_model=schemas.Jugador)
def crear_jugador(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.create_jugador(db, jugador)


@app.get("/jugadores", response_model=list[schemas.Jugador])
def listar_jugadores(db: Session = Depends(get_db)):
    return crud.get_jugadores(db)


@app.get("/jugadores/{jugador_id}", response_model=schemas.Jugador)
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud.get_jugador(db, jugador_id)
    if jugador is None:
        return {"error": "Jugador no encontrado"}
    return jugador
