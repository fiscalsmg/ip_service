import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.schemas.input_data import InputData


@pytest.fixture
def app() -> FastAPI:
    from app.main import app as fastapi_app

    yield fastapi_app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)


@pytest.fixture
def input_data() -> InputData:
    return InputData(ip="")
