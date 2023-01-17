import click
import requests
from tabulate import tabulate
from get_ip_info import get_ip_status_info, retrieve_all_ip_addresses

@click.command()
def average_stats():
    """ Command for returning average values of all service types """
    all_ip_addresses = retrieve_all_ip_addresses()
    stats = {}
    for ip in all_ip_addresses:
        response = requests.get(f"http://localhost:8080/{ip}")
        server_stats = response.json()
        service_name = server_stats['service']
        cpu = float(server_stats['cpu'][:-1])
        memory = float(server_stats['memory'][:-1])
        if service_name not in stats:
            stats[service_name] = {'cpu': cpu, 'memory': memory, 'count': 1}
        else:
            stats[service_name]['cpu'] += cpu
            stats[service_name]['memory'] += memory
            stats[service_name]['count'] += 1
    for service in stats:
        stats[service]['cpu'] = stats[service]['cpu'] / stats[service]['count']
        stats[service]['memory'] = stats[service]['memory'] / stats[service]['count']
    
    table = []
    for service, values in stats.items():
        table.append([service, values["cpu"], values["memory"], values["count"]])
    click.echo(tabulate(table, headers=["Service", "CPU", "Memory", "Count"], tablefmt="fancy_grid"))

if __name__ == '__main__':
    average_stats()
