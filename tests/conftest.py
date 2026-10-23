from collections.abc import Iterator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from legalization_consulting.core.config import Settings
from legalization_consulting.main import create_app


@pytest.fixture
def app() -> FastAPI:
    return create_app(settings=Settings(_env_file=None))


@pytest.fixture
def client(app: FastAPI) -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client
