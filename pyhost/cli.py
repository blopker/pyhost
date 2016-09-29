# -*- coding: utf-8 -*-

import click
from python_hosts import Hosts, HostsEntry

HOSTS_FILE = '/etc/hosts'


@click.group()
@click.option('--hosts', default=HOSTS_FILE, type=click.Path(exists=True))
@click.version_option()
def main(hosts):
    """Manage your hosts file"""
    global HOSTS_FILE
    HOSTS_FILE = hosts


@main.command()
def list():
    """ List current host entries """
    with open(HOSTS_FILE) as f:
        click.echo(f.read())


@main.command()
@click.argument('ip', type=str)
@click.argument('hosts', type=str, nargs=-1, required=True)
def set(ip, hosts):
    """ Set hosts to ip """
    hosts_file = Hosts(path=HOSTS_FILE)
    new_entry = HostsEntry(entry_type='ipv4', address=ip, names=hosts)
    hosts_file.add([new_entry])
    hosts_file.write()


@main.command()
@click.argument('ip', type=str)
def remove(ip):
    """ Remove ip from hosts """
    hosts_file = Hosts(path=HOSTS_FILE)
    hosts_file.remove_all_matching(ip)
    hosts_file.write()


if __name__ == "__main__":
    main()
