import pytest
from unittest.mock import patch
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


@patch("psutil.cpu_percent")
@patch("psutil.virtual_memory")
def test_high_usage_alert(mock_memory, mock_cpu, client):
    """Test alert message when CPU or memory is high"""

    mock_cpu.return_value = 90
    mock_memory.return_value.percent = 85

    response = client.get("/")

    assert response.status_code == 200
    assert b"High CPU or memory utilization detected!" in response.data