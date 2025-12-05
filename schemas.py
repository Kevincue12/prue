from pydantic import BaseModel
from datetime import date
from typing import Optional, List
import enum


# ==== ENUMS (API) ====

class EstadoJugadorAPI(str, enum.Enum):
    activo = "activo"
    lesionado = "lesionado"
    suspendido = "suspendido"


class PosicionJugadorAPI(str, enum.Enum):
    portero = "portero"
    defensa = "defensa"
    medio = "medio"
    delantero = "delantero"


class ResultadoPartidoAPI(str, enum.Enum):
    victoria = "victoria"
    empate = "empate"
    derrota = "derrota"


# ==== ESTADISTICA ====

class EstadisticaBase(BaseModel):
    minutos_jugados: int = 0
    goles_marcados: int = 0
    asistencias: int = 0
    tarjetas_amarillas: int = 0
    tarjetas_rojas: int = 0


class EstadisticaCreate(EstadisticaBase):
    jugador_id: int
    partido_id: int


class Estadistica(EstadisticaBase):
    id: int
    jugador_id: int
    partido_id: int

    model_config = {"from_attributes": True}


# ==== JUGADOR ====

class JugadorBase(BaseModel):
    nombre: str
    numero_camiseta: int
    nacionalidad: str
    fecha_nacimiento: date
    altura_cm: float
    peso_kg: float
    pie_dominante: str
    posicion: PosicionJugadorAPI
    estado: EstadoJugadorAPI = EstadoJugadorAPI.activo
    velocidad: Optional[float] = None
    resistencia: Optional[float] = None


class JugadorCreate(JugadorBase):
    pass


class Jugador(JugadorBase):
    id: int

    model_config = {"from_attributes": True}


# ==== PARTIDO ====

class PartidoBase(BaseModel):
    fecha: date
    rival: str
    es_local: bool = True
    goles_sigomota: int = 0
    goles_rival: int = 0
    resultado: ResultadoPartidoAPI
    resuelto_por_penales: bool = False


class PartidoCreate(PartidoBase):
    pass


class Partido(PartidoBase):
    id: int

    model_config = {"from_attributes": True}


# ==== RESPUESTAS COMPUESTAS ====

class EstadisticaDetallada(Estadistica):
    jugador: Jugador
    partido: Partido
