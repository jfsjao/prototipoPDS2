from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = "postgres"
password = "12345"
database = "nome_database"
host = "localhost"

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()