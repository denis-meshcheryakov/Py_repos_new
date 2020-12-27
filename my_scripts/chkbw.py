#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "chkbw.py"
#
import subprocess
import ipaddress
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
network = input('Введите подсеть: ')
net = ipaddress.ip_network(network)
ip = str(net[1])
print()
print('-' * 60)
print('ping ...')
print('-' * 60)
print()
ping = subprocess.run(['ping', '-s', '1500', '-i', '0.2', '-c', '5', ip], stdout=subprocess.PIPE, encoding='utf-8')
ping_result = str(ping.stdout)
ping_result = ping_result.split('\n')
for line in ping_result:
    if line.startswith('---'):
        print(line)
    elif 'packets transmitted' in line:
        print(line)
    elif 'rtt min/avg/max/mdev' in line:
        print(line)
print()
print('-' * 60)
print('Waiting for bandwidth ...')
print('-' * 60)



def send_show_command(device):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            model_of_router = ssh.find_prompt()
            if 'RTR-930' in model_of_router:
                interface_brief = 'display ip interface brief'
            else:
                interface_brief = 'show ip interface brief'
            if 'CO_' in model_of_router:
                band_width = '12M'
            else:
                band_width = '6M'
            iperf = subprocess.run(['iperf', '-c', ip, '-u', '-b', band_width, '-t', '5'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            interface_brief_output = ssh.send_command(interface_brief)
            for line in interface_brief_output.split('\n'):
                if ip in line:
                    intf = line.split()[0]
            if 'RTR-930' in model_of_router:
                bandwidth_command = 'do sh int {} | i input rate'.format(intf)
            else:
                bandwidth_command = 'do sh int {} | i input rate'.format(intf)
            ssh.config_mode()
            output = ssh.send_command(bandwidth_command, delay_factor=5)
            print()
            print('Input rate', model_of_router, 'is:')
            print(output)
            ssh.exit_config_mode()
            result = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    device = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
result = send_show_command(device)