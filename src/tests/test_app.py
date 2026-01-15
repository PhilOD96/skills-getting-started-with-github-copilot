import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Adjust based on your app's response


def test_another_endpoint():
    response = client.get("/another-endpoint")
    assert response.status_code == 200
    assert "expected_key" in response.json()
