import pytest
import requests
from click.testing import CliRunner
from unittest.mock import MagicMock
from get_ip_info import get_ip_status_info, ip_status, cli
from io import StringIO
import sys
from tabulate import tabulate

def test_get_ip_status_info_is_successful(mocker):    
    # Arrange
    mock_response = MagicMock()
    mock_response.json.return_value = {"cpu": "75%", "memory": "50%", "service": "test-service"}

    # Act
    mocker.patch.object(requests, 'get', return_value=mock_response)
    result = get_ip_status_info("8.8.8.8")

    # Assert
    assert result == ["8.8.8.8", "test-service", "Healthy", 75, 50]
    
def test_get_invalid_ip_status_info_is_unsuccessful(mocker):
    # Arrange
    mock_response = MagicMock()
    mock_response.json.return_value = {"error": "Invalid IP"}

    # Act
    mocker.patch.object(requests, 'get', return_value=mock_response)
    result = get_ip_status_info("8.8.8.8")

    # Assert
    assert result == ["8.8.8.8", "N/A", "NOT FOUND","N/A", "N/A"]
    
def test_get_multiple_ip_addresse_info_is_successful(mocker, capfd):
    ip_input = "8.8.8.8-8.8.8.9"
    mock_response = MagicMock()
    mock_response.json.side_effect = [
        {"cpu": "75%", "memory": "50%", "service": "test-service"},
        {"cpu": "50%", "memory": "90%", "service": "test-service-2"},
    ]
    
    expected_output = [
        ["IP", "Service", "Status", "CPU", "Memory"],
        ["8.8.8.8", "test-service", "Healthy", 75, 50],
        ["8.8.8.9", "test-service-2", "Unhealthy", 50, 90],
    ]

    # Use a mock for the get_ip_status_info function
    mocker.patch.object(requests, 'get', return_value=mock_response)
    runner = CliRunner()
    result = runner.invoke(ip_status, ["--ip_input", ip_input])
    assert result.output.strip() == tabulate(expected_output, headers="firstrow", tablefmt="fancy_grid").strip()