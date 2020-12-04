#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_to_vl_700.py"
#
import ipaddress
from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
n = input('''Если хотите добавить подсеть, нажмите Enter
Введите подсети и нажмите Enter:
________________________________________________________
Если хотите удалить подсеть, введите "no" и нажмите Enter
Введите подсети и нажмите Enter:
<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''')
print('*' * 57)
net = []
while True:
    net_input = input()
    if net_input:
        net.append(net_input)
    else:
        break

print('Connecting to CORE ...')
def get_commands(net, n):
    net_list = []
    commands = ['int fastEthernet 0/0.700']
    for line in net:
        line = ipaddress.ip_network(line)
        ip = str(line[1])
        mask = str(line.netmask)
        net_list.append([ip, mask])
        lin = '{} ip address {} {} secondary'.format(n, ip, mask)
        commands.append(lin)
    return commands

commands = get_commands(net, n)

def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_config_set(commands)
            output = output.strip()
            output_wr = ssh.send_command('write')
            result = output, output_wr
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_show_command(device, commands)
        pprint(result, width=120)