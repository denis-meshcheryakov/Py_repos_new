#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд port-security
 (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    """
    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона access_mode_template и
    port_security_template
    """
    result = []

    for intf, vlan in access_config.items():
        result.append(f'interface {intf}')
        for template in access_mode_template:
            if template.endswith('access vlan'):
                result.append(template + f'{vlan}')
            else:
                result.append(template)
                for line in port_security_template:
                    if psecurity is not None:
                        result.append(line)
    return result
for_print = generate_access_config(access_config, access_mode_template, psecurity = None)
print(for_print)