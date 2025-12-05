from sqlalchemy import (
    Column, Integer, String, Float, Date, Enum,
    Boolean, ForeignKey
)
from sqlalchemy.orm import relationship
from database import Base
import enum


# ==== ENUMS ====

class EstadoJugador(str, enum.Enum):
    activo = "activo"
    lesionado = "lesionado"
    suspendido = "suspendido"


class PosicionJugador(str, enum.Enum):
    portero = "portero"
    defensa = "defensa"
    medio = "medio"
    delantero = "delantero"


class ResultadoPartido(str, enum.Enum):
    victoria = "victoria"
    empate = "empate"
    derrota = "derrota"


# ==== MODELOS ====

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    numero_camiseta = Column(Integer, nullable=False)
    nacionalidad = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

    # Datos físicos / deportivos
    altura_cm = Column(Float)      # altura en cm
    peso_kg = Column(Float)        # peso en kg
    pie_dominante = Column(String)  # izquierda / derecha
    velocidad = Column(Float, nullable=True)   # opcional
    resistencia = Column(Float, nullable=True) # opcional

    posicion = Column(Enum(PosicionJugador), nullable=False)
    estado = Column(Enum(EstadoJugador), default=EstadoJugador.activo)

    # Relación con estadísticas por partido
    estadisticas = relationship("EstadisticaJugador", back_populates="jugador")


class Partido(Base):
    __tablename__ = "partidos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    rival = Column(String, nullable=False)
    es_local = Column(Boolean, default=True)

    goles_sigomota = Column(Integer, default=0)
    goles_rival = Column(Integer, default=0)

    resultado = Column(Enum(ResultadoPartido), nullable=False)

    resuelto_por_penales = Column(Boolean, default=False)

    estadisticas = relationship("EstadisticaJugador", back_populates="partido")


class EstadisticaJugador(Base):
    __tablename__ = "estadisticas_jugador"

    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"))
    partido_id = Column(Integer, ForeignKey("partidos.id"))

    minutos_jugados = Column(Integer, default=0)
    goles_marcados = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)
    tarjetas_amarillas = Column(Integer, default=0)
    tarjetas_rojas = Column(Integer, default=0)

    jugador = relationship("Jugador", back_populates="estadisticas")
    partido = relationship("Partido", back_populates="estadisticas")
