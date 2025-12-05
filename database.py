from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de Clever Cloud (TU BASE)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://uzcwxj3cucywbasjwhmf:0SK9XiT7Fehp8mAoLQiqboHfQTFOGX@b62ldgps597kj8wg8eq2-postgresql.services.clever-cloud.com:5432/b62ldgps597kj8wg8eq2?sslmode=require"
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
