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
ip = str(net[2])
print()
print('-' * 60)
print('ping ...')
print('-' * 60)
print()
ping = subprocess.run(['ping', '-s', '1500', '-i', '0.2', '-c', '100', ip],
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


def send_show_command(device):
    result = {}
	guesser = SSHDetect(**device)
	best_match = guesser.autodetect()
	print(best_match)  # Name of the best device_type to use further
	print(guesser.potential_matches)  # Dictionary of the whole matching result
	# Update the 'device' dictionary with the device_type
    try:
		device["device_type"] = best_match
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            model_of_router = ssh.find_prompt()
            if '930-RTR' in model_of_router:
                interface_brief = 'display ip interface brief'
            else:
                interface_brief = 'show ip interface brief'
            if 'CO_' in model_of_router:
                band_width = '12M'
            else:
                band_width = '6M'
            iperf = subprocess.run(['iperf', '-c', ip, '-u', '-b', band_width, '-t', '30'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            interface_brief_output = ssh.send_command(interface_brief)
            for line in interface_brief_output.split('\n'):
                if ip in line:
                    intf = line.split()[0]
                    if intf == 'GE0/0':
                        intf = 'GigabitEthernet0/0'
            if '930-RTR' in model_of_router:
                bandwidth_command = 'display interface {} | i input'.format(intf)
            else:
				 bandwidth_command = 'do sh int {} | i input rate'.format(intf)
            ssh.config_mode()
            output = ssh.send_command(bandwidth_command)
            print()
            print('Input rate', model_of_router, 'is:')
            print()
            print(output)
            ssh.exit_config_mode()
            result = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    device = {
    "device_type": "autodetect",
    "ip": ip,
    "username": "localadmin",
    "password": "X5remset",
    }
result = send_show_command(device)
