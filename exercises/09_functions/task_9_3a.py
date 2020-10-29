#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    """ Функция обрабатывает конфигурационный файл коммутатора
    и возвращает кортеж из двух словарей
    """
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as src:
        for line in src:
            if line.startswith('interface FastEthernet'):
               intf = line.split()[-1]
            elif 'access vlan' in line:
                vlan = int(line.split()[-1])
                access_dict[intf] = vlan
            elif 'switchport mode access' in line and not 'access vlan' in line:
                vlan = 1
                access_dict[intf] = vlan
            elif 'allowed vlan' in line:
                vlan = line.split()[-1]
                vlan = vlan.split(',')
                vlan = [int(vlan) for vlan in vlan]
                trunk_dict[intf] = vlan
            result = (access_dict, trunk_dict)
    return result
print(get_int_vlan_map('config_sw2.txt'))