import os

# Tests run against a real PostgreSQL instance. Point DATABASE_URL at a
# throwaway test database (CI provides one via a postgres service container).
_TEST_DB = os.environ.get("TEST_DATABASE_URL") or os.environ.get("DATABASE_URL")
if not _TEST_DB:
    raise RuntimeError(
        "Set TEST_DATABASE_URL (or DATABASE_URL) to a PostgreSQL URL to run the tests."
    )
os.environ["DATABASE_URL"] = _TEST_DB
os.environ.setdefault("SECRET_KEY", "test-secret-key-at-least-32-bytes-long!!")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("GROQ_API_KEY", "test-groq-key")

import pytest
from fastapi.testclient import TestClient

from main import app
from src.config.db import Base, engine


@pytest.fixture(autouse=True)
def _fresh_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


def _signup_payload(**over):
    data = {
        "firstname": "Test",
        "lastname": "User",
        "email": "test@example.com",
        "hashed_password": "password123",
        "created_at": "2026-01-01T00:00:00",
    }
    data.update(over)
    return data


@pytest.fixture
def signup_payload():
    return _signup_payload


@pytest.fixture
def auth_headers(client):
    client.post("/user/signup", json=_signup_payload())
    r = client.post("/user/login", json={"email": "test@example.com", "password": "password123"})
    token = r.json()["user"]["token"]
    return {"Authorization": f"Bearer {token}"}
