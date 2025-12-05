from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de Clever Cloud (TU BASE)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://ujnown9kpj5ra3to3gmc:NSV2tXHsATz97mYVP3gAcPgUkGn9dn@bxmeg2vi6up3d1amzvyk-postgresql.services.clever-cloud.com:5432/bxmeg2vi6up3d1amzvyk"
)

# Crear motor con pre_ping
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Crear sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base
Base = declarative_base()


# Dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
