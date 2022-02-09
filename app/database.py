from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"


# an Engine, which the Session will use for connection

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# A database session/connection
# Each instance of the SessionLocal class will be a database session.
# The class itself is not a database session yet.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# We will inherit from this class to create each of the database
# models or classes (the ORM models):

Base = declarative_base()


# Dependency

# Dependency will create a new SQLAlchemy SessionLocal that will be used in 
# a single request,
# and then close it once the request is finished.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()