from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = (
    "postgresql+psycopg://postgres:DB_PASSWORD"
    "@localhost:5432/bashkir_dictionary"
)

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass