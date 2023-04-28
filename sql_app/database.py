from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.environ.get('DATABASE_URL')

# -- SQLlite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  

# -- postgresSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"  

# -- MySQL
SQLALCHEMY_DATABASE_URL = database_url 


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
