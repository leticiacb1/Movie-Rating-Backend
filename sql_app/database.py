from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -- SQLlite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  

# -- postgresSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"  

# -- MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/serversiderendering" 


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
