"""
This module contains tests for the Flask application in aschatbotflask.
It ensures proper functionality of the app's routes and responses.
"""

import pytest
from aschatbotflask import app  # Import your Flask app


@pytest.fixture

def client1():

    """
    Provides a test client for the Flask application.
    """
    # Flask provides a way to create a test client
    with app.test_client() as client:
        yield client

def test_hello_world(client2):
    """
    Tests the root ("/") route of the Flask application.
    Ensures the status code is 200 and the response contains the expected text.
    """
    # Make a GET request to the root URL "/"
    response = client2.get('/')
    # Assert that the response data matches the expected output
    assert response.status_code == 200
    assert b"Your OpenAI API Key:" in response.data
