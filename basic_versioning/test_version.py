"""
Unit test for verifying the application version output.
"""

import pytest
from basic_versioning.app import app

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_version(client):
    """Test that the /version endpoint returns the correct version."""
    response = client.get("/version")  # Send GET request to /version
    assert response.status_code == 200
    assert response.get_json() == {"version": "v0.0.1"}
