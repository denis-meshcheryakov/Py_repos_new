#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "test_bw.py"
#
import subprocess
import ipaddress
from netmiko import SSHDetect, ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from netmiko.ssh_exception import  AuthenticationException

network = input('Введите подсеть: ')
net = ipaddress.ip_network(network)
ip = str(net[1])
print()
print('-' * 60)
print('ping, ping, ping ...')
print('-' * 60)
print()
ping = subprocess.run(['ping', '-s', '1500', '-i', '0.2', '-c', '10', ip],
stdout=subprocess.PIPE, encoding='utf-8')

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

cisco = {
    "device_type": "cisco_ios",
    "ip": ip,
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }
hpe = {
    "device_type": "hp_comware",
    "ip": ip,
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }

for device in (cisco, hpe):
    try:
        with ConnectHandler(**device) as ssh:
            model_of_router = ssh.find_prompt()
            print(model_of_router)
            ssh.disconnect()
        #return model_of_router
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


#model_of_router = get_vendor(device)
if '930-RTR' in model_of_router:
    vendor = 'hp_comware'
else:
    vendor = 'cisco_ios'
print(vendor)

device = {
    "device_type": vendor,
    "ip": ip,
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }

def send_show_command(device):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            model_of_router = ssh.find_prompt()
            if '930-RTR' in model_of_router:
                interface_brief = 'display ip interface brief'
            else:
                interface_brief = 'show ip interface brief'
            print(interface_brief)
            if 'CO_' in model_of_router:
                band_width = '12M'
            else:
                band_width = '6M'
            iperf = subprocess.run(['iperf', '-c', ip, '-u', '-b', band_width, '-t', '30'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            interface_brief_output = ssh.send_command(interface_brief)
            print(interface_brief_output)
            for line in interface_brief_output.split('\n'):
                if ip in line:
                    intf = line.split()[0]
                    if intf == 'GE0/0':
                        intf = 'GigabitEthernet0/0'
            if '930-RTR' in model_of_router:
                bandwidth_command = 'display interface {} | i input '.format(intf)
            else:
                bandwidth_command = 'do sh int {} | i input rate'.format(intf)
            #print(bandwidth_command)
            ssh.config_mode()
            output = ssh.send_command(bandwidth_command)
            print()
            print('Input rate', model_of_router, 'is:')
            print(output)
            ssh.exit_config_mode()
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    result = send_show_command(device)
