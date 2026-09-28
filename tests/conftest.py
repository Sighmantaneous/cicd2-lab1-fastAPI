import pytest
from fastapi.testclient import TestClient

from app.main import apps, users 

@pytest.fixtures(autouse=True)
def clear_users():
    users.clear()


@pytest.fixture
def client():
    return TestClient(app)
