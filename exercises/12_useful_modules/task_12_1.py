#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


import subprocess
from pprint import pprint
from threading import Thread

ip_list = ['192.168.74.2', '192.168.100.100',
'8.8.8.8', '8.8.4.4', '10.10.10.10',
'20.20.20.20', '30.30.30.30', '40.40.40.40']

def ping_ip_addresses(ip_list):
    reach_list = []
    unreach_list = []
    for ip in ip_list:
        reply = subprocess.run(['ping', '-c', '3', '-n', '-i', '0.2', ip],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
        if reply.returncode == 0:
            reach_list.append(ip)
        else:
            unreach_list.append(ip)
        result = reach_list, unreach_list
    return result

if __name__ == "__main__":
    print("*" * 30)
    pprint(ping_ip_addresses(ip_list))

