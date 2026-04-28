import sys
import os

# ✅ Fix path FIRST
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ THEN import
from app import app

import pytest


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home_route_status(client):
    """Test if homepage loads successfully"""
    response = client.get("/")
    assert response.status_code == 200


def test_home_route_content(client):
    """Test if response contains expected content"""
    response = client.get("/")
    assert b"CPU" in response.data or b"cpu" in response.data


def test_invalid_route(client):
    """Test invalid route returns 404"""
    response = client.get("/invalid")
    assert response.status_code == 404