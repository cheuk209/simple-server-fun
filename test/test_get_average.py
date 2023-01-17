import pytest
import requests
from click.testing import CliRunner
from unittest.mock import MagicMock
from get_average import average_stats, retrieve_all_ip_addresses
from tabulate import tabulate
import json
import mock

def test_retrieve_all_ip_addresses_is_successful(mocker):
    expected_value = ["8.8.8.8", "8.8.8.9", "8.8.8.10"]
    mock_response = MagicMock()
    mock_response.json.return_value = ["8.8.8.8", "8.8.8.9", "8.8.8.10"]
    
    mocker.patch.object(requests, 'get', return_value=mock_response)
    result = retrieve_all_ip_addresses()
    
    assert result == expected_value

@mock.patch("get_average.retrieve_all_ip_addresses")
@mock.patch('requests.get')
def test_average_stats(mock_get, retrieve_all_ip_addresses):
    # Create a list of mock IP addresses
    mock_ips = ['10.58.1.1', '10.58.1.2', '10.58.1.3']

    # Create a list of mock server statistics
    mock_stats = [
        {"cpu": "75%", "memory": "50%", "service": "PermissionsService"},
        {"cpu": "50%", "memory": "30%", "service": "AuthService"},
        {"cpu": "35%", "memory": "25%", "service": "PermissionsService"}
    ]
    # Create a mock function to simulate the behavior of the requests.get function
    mock_get.return_value = MagicMock()
    mock_get.return_value.json.side_effect = mock_stats

    # Use the unittest.mock.patch to replace the retrieve_all_ip_addresses function
    retrieve_all_ip_addresses.return_value = mock_ips

    # Call the average_stats function and capture the output
    runner = CliRunner()
    result = runner.invoke(average_stats)

    # Assert that the output matches the expected output
    expected_output = [
        ["Service", "CPU", "Memory", "Count"],
        ["PermissionsService", 55.0, 37.5, 2],
        ["AuthService", 50.0, 30.0, 1]
    ]
    assert result.output.strip() == tabulate(expected_output, headers="firstrow", tablefmt="fancy_grid").strip()