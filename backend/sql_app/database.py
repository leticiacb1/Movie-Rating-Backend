from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@127.0.0.1:3306/movies_ratings"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Cria uma sessão no banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

Base = declarative_base()