from typing import Generator

from starlette.testclient import TestClient
import pytest

from app.main import app
from app.repositories.orm import SessionLocal


@pytest.fixture(scope='module')
def client():
    with TestClient(app) as client:
        yield client