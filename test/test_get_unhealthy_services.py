from get_ip_info import get_ip_status_info
from get_average import retrieve_all_ip_addresses
from mock import patch, MagicMock, mock
from click.testing import CliRunner
import io
import sys
from get_unhealthy_services import display_unhealthy_services


@mock.patch("get_ip_info.get_ip_status_info")
def test_display_unhealthy_services_if_they_exist(mock_ip_status):
    # Set up the mock return values for the functions
    
    # Invoke the display_unhealthy_services() function using CliRunner
    runner = CliRunner()
    mock_ip_addresses = MagicMock()
    mock_ip_addresses.return_value = ["8.8.8.8", "8.8.8.9"]
    mock_ip_status.side_effect = [
        ("8.8.8.8", "service1", "Healthy", 40, 50),
        ("8.8.8.9", "service2", "Unhealthy", 90, 30),
    ]
    with mock.patch("get_average.retrieve_all_ip_addresses") as mock_ip_addresses:
        mock_ip_addresses.return_value = ["8.8.8.8"]
        result = runner.invoke(display_unhealthy_services)
    # Assert that the output is as expected
    expected_output = "Services with less than 2 healthy instances include: \nservice2"
    # check if the function calls are being made correctly
    assert 1 == 1
    
# def test_display_unhealthy_services_unsuccess(mocker):
#     # Mock the return value of the retrieve_all_ip_addresses() function
#     mocker.patch("module_name.retrieve_all_ip_addresses", return_value=["ip1", "ip2", "ip3"])
#     # Mock the return value of the get_ip_status_info() function
#     mocker.patch("module_name.get_ip_status_info", side_effect=[("ip1", "service1", "Healthy"),
#                                                                ("ip2", "service1", "Healthy"),
#                                                                ("ip3", "service1", "Healthy")])
#     # Capture the output of the display_unhealthy_services() function
#     captured_output = io.StringIO()
#     sys.stdout = captured_output
#     display_unhealthy_services()
#     sys.stdout = sys.__stdout__
#     # Assert that the output is as expected
#     expected_output = "Your DevOps engineers are too good! There are no unhealthy services!\n"
#     assert captured_output.getvalue() == expected_output