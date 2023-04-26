from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Neste exemplo, estamos "conectando" a um banco de dados SQLite (abrindo um arquivo com o banco de dados SQLite). 
# #O arquivo estará localizado no mesmo diretório do arquivo sql_app.db :
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"   
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # connect_args={"check_same_thread": False} --- Only SQLite
)

# Cria uma sessão no banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

Base = declarative_base()  # Herdamos desta classe para criar cada um dos modelos ou classes de banco de dados

#SQLAlchemy usa o termo "modelo" para se referir a instâncias que interagem com o banco de dados.