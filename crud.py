from sqlalchemy.orm import Session
from models import Jugador, Estadistica
from schemas import JugadorCreate


def create_jugador(db: Session, jugador: JugadorCreate):
    db_jugador = Jugador(
        nombre=jugador.nombre,
        fecha_nacimiento=jugador.fecha_nacimiento,
        numero=jugador.numero,
        nacionalidad=jugador.nacionalidad,
        altura=jugador.altura,
        peso=jugador.peso,
        pie_dominante=jugador.pie_dominante,
        posicion=jugador.posicion,
        estado=jugador.estado
    )
    db.add(db_jugador)
    db.commit()
    db.refresh(db_jugador)

    # Crear estadistica
    db_est = Estadistica(
        jugador_id=db_jugador.id,
        goles_marcados=jugador.estadistica.goles_marcados,
        asistencias=jugador.estadistica.asistencias,
        minutos_jugados=jugador.estadistica.minutos_jugados,
        tarjetas_amarillas=jugador.estadistica.tarjetas_amarillas,
        tarjetas_rojas=jugador.estadistica.tarjetas_rojas
    )
    db.add(db_est)
    db.commit()
    db.refresh(db_est)

    return db_jugador


def get_jugadores(db: Session):
    return db.query(Jugador).all()


def get_jugador(db: Session, jugador_id: int):
    return db.query(Jugador).filter(Jugador.id == jugador_id).first()
