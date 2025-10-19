import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """Test the hello world endpoint returns 200 status code"""
    response = client.get("/")
    assert response.status_code == 200


def test_hello_world_content(client):
    """Test the hello world endpoint returns correct content"""
    response = client.get("/")
    assert b"Hello, World!" in response.data
    assert b"Welcome to Flask!" in response.data


def test_hello_world_content_type(client):
    """Test the hello world endpoint returns HTML content type"""
    response = client.get("/")
    assert "text/html" in response.content_type
