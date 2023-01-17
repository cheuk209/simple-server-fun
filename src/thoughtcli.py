import click
from get_average import average_stats
from get_ip_info import ip_status
from get_unhealthy_services import display_unhealthy_services

@click.group()
def cli():
    pass

cli.add_command(average_stats)
cli.add_command(ip_status)
cli.add_command(display_unhealthy_services)

if __name__ == '__main__':
    cli()