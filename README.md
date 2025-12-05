# Proyecto de sigmotoaFC

Este proyecto es una API construida en **FastAPI** para administrar jugadores, partidos y estadísticas deportivas. Permite crear, listar, actualizar y eliminar información, así como relacionar jugadores con partidos mediante estadísticas detalladas.

---

##  Descripción 

La API maneja tres entidades principales:

* Jugadores
* Partidos
* Estadísticas por partido
  
---

## 🛠️ Tecnologías Utilizadas

* **Python 3.10+**
* **FastAPI**
* **SQLAlchemy / ORM**
* **Pydantic** para validación de datos
* **SQLite / PostgreSQL (dependiendo la configuración)**
* **Uvicorn** como servidor ASGI

---

## 📦 Instalación

### 1️⃣ Clona el repositorio

```
git clone https://github.com/Kevincue12/Final_DEV_1
cd Final_DEV_1
```

### 2️⃣ Crea un entorno virtual

```
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3️⃣ Instala dependencias

```
pip install -r requirements.txt
```

### 4️⃣ Configura la base de datos

En `database.py` ajusta la URL según tu motor SQL.

Ejemplo para SQLite:

```
DATABASE_URL = "sqlite:///./app.db"
```

Ejemplo para PostgreSQL:

```
DATABASE_URL = "postgresql://user:password@host/dbname"
```

---

## ▶️ Ejecución del proyecto

Inicia el servidor con:

```
uvicorn main:app --reload
```

Luego abre la documentación interactiva:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

##  Mapa de Endpoints

###  Jugadores (`/jugadores`)

| Método | Endpoint          | Descripción                |
| ------ | ----------------- | -------------------------- |
| GET    | `/jugadores/`     | Listar todos los jugadores |
| POST   | `/jugadores/`     | Crear un nuevo jugador     |
| GET    | `/jugadores/{id}` | Obtener un jugador por ID  |
| PUT    | `/jugadores/{id}` | Actualizar un jugador      |
| DELETE | `/jugadores/{id}` | Eliminar un jugador        |

---

###  Partidos (`/partidos`)

| Método | Endpoint         | Descripción            |
| ------ | ---------------- | ---------------------- |
| GET    | `/partidos/`     | Listar partidos        |
| POST   | `/partidos/`     | Crear un partido       |
| GET    | `/partidos/{id}` | Obtener partido por ID |
| PUT    | `/partidos/{id}` | Actualizar un partido  |
| DELETE | `/partidos/{id}` | Eliminar un partido    |

---

###  Estadísticas (`/estadisticas`)

| Método | Endpoint                             | Descripción                                    |
| ------ | ------------------------------------ | ---------------------------------------------- |
| POST   | `/estadisticas/`                     | Crear estadísticas de un jugador en un partido |
| GET    | `/estadisticas/jugador/{jugador_id}` | Listar estadísticas de un jugador              |
| GET    | `/estadisticas/partido/{partido_id}` | Listar estadísticas de un partido              |

---

##  Modelos Principales

### Jugador

* Nombre
* Número de camiseta
* Nacionalidad
* Fecha de nacimiento
* Altura, peso
* Pie dominante
* Posición
* Estado

### Partido

* Fecha
* Rival
* Local o visitante
* Goles equipo vs rival
* Resultado

### EstadísticaJugador

* Minutos jugados
* Goles
* Asistencias
* Tarjetas
* Relación jugador ↔ partido

---

## Autores
* Kevin Cuevas - 67001396
* Nicole Nieto - 67001296
Proyecto desarrollado como parte de un módulo académico de desarrollo de software.
