from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum


# ===== ENUMS =====
class EstadoJugador(str, enum.Enum):
    activo = "activo"
    lesionado = "lesionado"
    suspendido = "suspendido"


class PosicionJugador(str, enum.Enum):
    portero = "portero"
    defensa = "defensa"
    medio = "medio"
    delantero = "delantero"


# ===== ESTADISTICA =====
class Estadistica(Base):
    __tablename__ = "estadisticas"

    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"))
    goles_marcados = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)
    minutos_jugados = Column(Integer, default=0)
    tarjetas_amarillas = Column(Integer, default=0)
    tarjetas_rojas = Column(Integer, default=0)


# ===== JUGADOR =====
class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    numero = Column(Integer, nullable=False)
    nacionalidad = Column(String, nullable=False)
    altura = Column(Float)
    peso = Column(Float)
    pie_dominante = Column(String)

    estado = Column(Enum(EstadoJugador), default=EstadoJugador.activo)
    posicion = Column(Enum(PosicionJugador), nullable=False)

    estadistica = relationship("Estadistica", backref="jugador", uselist=False)
