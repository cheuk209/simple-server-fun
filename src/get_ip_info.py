import click
import requests
from tabulate import tabulate

@click.group()
def cli():
    pass

@click.command()
@click.option('--ip_input', required=True, help='The range of IP addresses to query.')
def ip_status(ip_input):
    """Command to query a range of IP addresses and return a table of information."""
    
    data = [["IP", "Service", "Status", "CPU", "Memory"]]
    if "-" in ip_input:
        start, end = ip_input.split("-")
        ips = [f"{start.split('.')[0]}.{start.split('.')[1]}.{start.split('.')[2]}.{i}" for i in range(int(start.split(".")[3]), int(end.split(".")[3])+1)]
    elif ip_input == "all":
        ips = retrieve_all_ip_addresses()
    else:
        ips = [ip_input]
        
    for ip in ips:
        ip_info = get_ip_status_info(ip) 
        # Append information to table data
        data.append(ip_info)

    # Print the table to the console
    click.echo(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))

def get_ip_status_info(ip):
    """Helper function to get the status data for an IP address."""
    response = requests.get(f"http://localhost:8080/{ip}")
    ip_info = response.json()
    try:
        cpu = int(ip_info["cpu"].strip("%"))
        memory = int(ip_info["memory"].strip("%"))
        return [ip, ip_info.get("service"), "Healthy" if cpu < 85 and memory < 85 else "Unhealthy", cpu, memory]
    except:
        print(f"Error getting status for {ip}")
        return [ip, "N/A", "NOT FOUND", "N/A", "N/A"]
    
def retrieve_all_ip_addresses():
    """ Helper function to get all IP addresses """
    response = requests.get(f"http://localhost:8080/servers")
    all_ip_addresses = response.json()
    return all_ip_addresses

cli.add_command(ip_status)

if __name__ == '__main__':
    ip_status()