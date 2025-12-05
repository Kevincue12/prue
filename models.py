from sqlalchemy import (
    Column, Integer, String, Float, Date, Enum,
    Boolean, ForeignKey
)
from sqlalchemy.orm import relationship
from database import Base
from datetime import date
import enum


# ==============================
#         🎯 ENUMS
# ==============================

class EstadoJugador(str, enum.Enum):
    activo = "Activo"
    lesionado = "Lesionado"
    suspendido = "Suspendido"


class PieDominante(str, enum.Enum):
    izquierdo = "Izquierdo"
    derecho = "Derecho"


class PosicionJugador(str, enum.Enum):
    ARQUERO = "Arquero"
    DEFENSA_C = "Defensa Central"
    DEFENSA_L = "Defensa Lateral"
    VOLANTE_D = "Volante Defensivo"
    VOLANTE_O = "Volante Ofensivo"
    VOLANTE_C = "Volante Central"
    VOLANTE_E = "Volante Extremo"
    DELANTERO_C = "Delantero Central"
    DELANTERO_P = "Delantero Punta"


class ResultadoPartido(str, enum.Enum):
    victoria = "victoria"
    empate = "empate"
    derrota = "derrota"


# ==============================
#         👟 JUGADOR
# ==============================

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    numero_camiseta = Column(Integer, nullable=False)
    nacionalidad = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

    # Datos físicos
    altura_cm = Column(Float, nullable=False)
    peso_kg = Column(Float, nullable=False)
    pie_dominante = Column(Enum(PieDominante), nullable=False)

    velocidad = Column(Float, nullable=True)
    resistencia = Column(Float, nullable=True)

    posicion = Column(Enum(PosicionJugador), nullable=False)
    estado = Column(Enum(EstadoJugador), default=EstadoJugador.activo)

    # Relación con estadísticas
    estadisticas = relationship("EstadisticaJugador", back_populates="jugador")

    @property
    def edad(self):
        """ Calcula edad exacta según fecha de nacimiento """
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )


# ==============================
#         ⚽ PARTIDO
# ==============================

class Partido(Base):
    __tablename__ = "partidos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    rival = Column(String, nullable=False)
    es_local = Column(Boolean, default=True)

    goles_sigomota = Column(Integer, default=0)
    goles_rival = Column(Integer, default=0)

    resultado = Column(Enum(ResultadoPartido), nullable=False)

    # ⚠️ Lo dejé porque estaba en tu código
    # Si lo vas a quitar completamente, dime y te lo limpio del proyecto
    resuelto_por_penales = Column(Boolean, default=False)

    estadisticas = relationship("EstadisticaJugador", back_populates="partido")


# ==============================
#      📊 ESTADISTICA JUGADOR
# ==============================

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
