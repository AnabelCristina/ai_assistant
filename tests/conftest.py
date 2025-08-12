import pytest
from unittest.mock import AsyncMock
from main import app
from fastapi.testclient import TestClient

@pytest.fixture
def mock_groq_service():
    mock = AsyncMock()
    mock.generate_response.return_value = "service answer"
    return mock

@pytest.fixture
def test_client():
    return TestClient(app)