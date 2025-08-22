import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base
from pytest import fixture
from alembic import command

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time




# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:abc123@localhost:5432/fastapi-test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}-test'



engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




#Dependency

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db




# client = TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()




@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    # command.upgrade("head")
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # command.downgrade("base")
    
