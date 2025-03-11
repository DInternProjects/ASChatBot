import pytest
from chatai import app  # Import your Flask app

@pytest.fixture
def client():
    # Flask provides a way to create a test client
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    # Make a GET request to the root URL "/"
    response = client.get('/')
    # Assert that the response data matches the expected output
    assert response.status_code == 200
    assert b"Your OpenAI API Key:" in response.data

