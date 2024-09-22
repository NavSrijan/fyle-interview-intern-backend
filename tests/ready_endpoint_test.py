import pytest
from flask import json


def test_ready_endpoint(client):
    """Test the readiness endpoint."""
    response = client.get('/')
    
    assert response.status_code == 200  # Check for HTTP 200 OK
    data = json.loads(response.data)  # Parse the JSON response
    assert data['status'] == 'ready'  # Check the status
    assert 'time' in data  # Ensure the time field is present
