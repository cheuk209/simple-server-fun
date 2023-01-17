from get_ip_info import get_ip_status_info
from tabulate import tabulate
import requests
import click
from get_average import retrieve_all_ip_addresses

@click.command()
def display_unhealthy_services():
    healthy_entries = {}
    unhealthy_services = []
    all_ip_addresses = retrieve_all_ip_addresses()
    print("Fish", all_ip_addresses)
    for ip in all_ip_addresses:
        ip_info = get_ip_status_info(ip)
        if ip_info[2] == "Healthy":
            if ip_info[1] not in healthy_entries:
                healthy_entries[ip_info[1]] = 1
            else:
                healthy_entries[ip_info[1]] += 1
    for key, values in healthy_entries.items():
        if values < 2:
            unhealthy_services.append(key)
    output_string = "\n".join(unhealthy_services)
    if output_string != "":
        click.echo("Services with less than 2 healthy instances include: ")
        click.echo(output_string)
    else:
        click.secho("Your DevOps engineers are too good! There are no unhealthy services!",fg="black", bg="yellow") 
    
if __name__ == '__main__':
    display_unhealthy_services()