# All fixtures available in this file are made available to all test files automatically
import pytest
from fastapi.testclient import TestClient

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app

from app.config import settings
from app.database import get_db
from app.database import Base
from app import models
from alembic import command


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_app.db"


# an Engine, which the Session will use for connection

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    """
    Every time a test is run, we create and drop tables, connect to a testing database,
    and use it for all the tests,
    so we create a database connection that is independent of the main app.
    """
    # Create the database

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    # We need to have an independent database session/connection (SessionLocal) per request,
    # use the same session through all the request and then close it after the request is finished.
    # And then a new session will be created for the next request.

    # yield is just like return - it returns whatever you tell it to (as a generator). The difference is
    # that the next time you call the generator, execution starts from the last call to the yield statement.
    #  Unlike return, the stack frame is not cleaned up when a yield occurs, however control is
    # transferred back to the caller, so its state will resume the next time the function is called.
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    """

    Connects to the new test database and overrides the initial database
    connection set for the main app

    """

    # Dependency override

    def override_get_db():
        try:
            # yield is a keyword that is used like return,
            # except the function will return a generator.
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


@pytest.fixture()
def init_posts(session):

    posts_data = [{"title": "1st title", "content": "1st content"},
        {"title": "2nd title", "content": "2nd content"},
        {"title": "3rd title", "content": "3rd content"},
        {"title": "4th title", "content": "4th content"}]

    # Validate posts according to the Post schema

    def create_post_model(post):
        return models.Post(**post)

    # map() -> built-in function that allows you to process and transform all 
    # the items in an iterable without using an explicit for loop, 

    # useful when you need to apply a transformation function to 
    # each item in an iterable and transform them into a new iterable
    
    # Here we convert each item in the array of post dicts ( post_data ) to Post model.

    mapped_posts = map(create_post_model, posts_data)
    posts = list(mapped_posts)

    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()

    # Returns an sqlalchemy model
    return posts
