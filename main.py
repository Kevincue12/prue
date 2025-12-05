from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import crud
import schemas

# Crear tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sigomota FC - Gestión de jugadores y partidos")

templates = Jinja2Templates(directory="templates")


# ===== RUTAS HTML =====

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@app.get("/jugadores_page", response_class=HTMLResponse)
def jugadores_page(request: Request, db: Session = Depends(get_db)):
    jugadores = crud.listar_jugadores(db)
    return templates.TemplateResponse(
        "jugadores_list.html",
        {"request": request, "jugadores": jugadores}
    )


@app.get("/jugadores/nuevo", response_class=HTMLResponse)
def jugadores_form(request: Request):
    return templates.TemplateResponse(
        "jugadores_form.html",
        {"request": request}
    )


@app.post("/jugadores/nuevo")
def crear_jugador_html(
    request: Request,
    nombre: str = Form(...),
    numero_camiseta: int = Form(...),
    nacionalidad: str = Form(...),
    fecha_nacimiento: str = Form(...),
    altura_cm: float = Form(...),
    peso_kg: float = Form(...),
    pie_dominante: str = Form(...),
    posicion: str = Form(...),
    db: Session = Depends(get_db),
):
    jugador_in = schemas.JugadorCreate(
        nombre=nombre,
        numero_camiseta=numero_camiseta,
        nacionalidad=nacionalidad,
        fecha_nacimiento=fecha_nacimiento,
        altura_cm=altura_cm,
        peso_kg=peso_kg,
        pie_dominante=pie_dominante,
        posicion=posicion,
        estado="activo"
    )
    crud.crear_jugador(db, jugador_in)
    return RedirectResponse(url="/jugadores_page", status_code=303)


@app.get("/partidos_page", response_class=HTMLResponse)
def partidos_page(request: Request, db: Session = Depends(get_db)):
    partidos = crud.listar_partidos(db)
    return templates.TemplateResponse(
        "partidos_list.html",
        {"request": request, "partidos": partidos}
    )


@app.get("/partidos/nuevo", response_class=HTMLResponse)
def partidos_form(request: Request):
    return templates.TemplateResponse(
        "partidos_form.html",
        {"request": request}
    )


@app.post("/partidos/nuevo")
def crear_partido_html(
    request: Request,
    fecha: str = Form(...),
    rival: str = Form(...),
    es_local: bool = Form(...),
    goles_sigomota: int = Form(0),
    goles_rival: int = Form(0),
    resultado: str = Form(...),
    resuelto_por_penales: bool = Form(False),
    db: Session = Depends(get_db),
):
    partido_in = schemas.PartidoCreate(
        fecha=fecha,
        rival=rival,
        es_local=es_local,
        goles_sigomota=goles_sigomota,
        goles_rival=goles_rival,
        resultado=resultado,
        resuelto_por_penales=resuelto_por_penales,
    )
    crud.crear_partido(db, partido_in)
    return RedirectResponse(url="/partidos_page", status_code=303)


# ===== RUTAS API (JSON) =====

@app.post("/api/jugadores", response_model=schemas.Jugador)
def crear_jugador_api(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.crear_jugador(db, jugador)


@app.get("/api/jugadores", response_model=list[schemas.Jugador])
def listar_jugadores_api(db: Session = Depends(get_db)):
    return crud.listar_jugadores(db)


@app.get("/api/jugadores/{jugador_id}", response_model=schemas.Jugador)
def obtener_jugador_api(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud.obtener_jugador(db, jugador_id)
    return jugador


@app.post("/api/partidos", response_model=schemas.Partido)
def crear_partido_api(partido: schemas.PartidoCreate, db: Session = Depends(get_db)):
    return crud.crear_partido(db, partido)


@app.get("/api/partidos", response_model=list[schemas.Partido])
def listar_partidos_api(db: Session = Depends(get_db)):
    return crud.listar_partidos(db)


@app.post("/api/estadisticas", response_model=schemas.Estadistica)
def crear_estadistica_api(est: schemas.EstadisticaCreate, db: Session = Depends(get_db)):
    return crud.crear_estadistica(db, est)


@app.get("/api/estadisticas/jugador/{jugador_id}", response_model=list[schemas.Estadistica])
def estadisticas_por_jugador(jugador_id: int, db: Session = Depends(get_db)):
    return crud.listar_estadisticas_por_jugador(db, jugador_id)


@app.get("/api/estadisticas/partido/{partido_id}", response_model=list[schemas.Estadistica])
def estadisticas_por_partido(partido_id: int, db: Session = Depends(get_db)):
    return crud.listar_estadisticas_por_partido(db, partido_id)
