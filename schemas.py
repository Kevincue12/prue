from pydantic import BaseModel
from datetime import date
from typing import Optional
import enum


# ===== ENUMS (para API) =====
class States(str, enum.Enum):
    activo = "activo"
    lesionado = "lesionado"
    suspendido = "suspendido"


class Position(str, enum.Enum):
    portero = "portero"
    defensa = "defensa"
    medio = "medio"
    delantero = "delantero"


# ===== ESTADISTICA =====
class EstadisticaBase(BaseModel):
    goles_marcados: int = 0
    asistencias: int = 0
    minutos_jugados: int = 0
    tarjetas_amarillas: int = 0
    tarjetas_rojas: int = 0


class Estadistica(EstadisticaBase):
    id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }


# ===== JUGADOR =====
class JugadorBase(BaseModel):
    nombre: str
    fecha_nacimiento: date
    numero: int
    nacionalidad: str
    altura: float
    peso: float
    pie_dominante: str
    posicion: Position
    estado: States = States.activo


class JugadorCreate(JugadorBase):
    estadistica: EstadisticaBase = EstadisticaBase()


class Jugador(JugadorBase):
    id: int
    estadistica: Optional[Estadistica]

    model_config = {
        "from_attributes": True
    }
