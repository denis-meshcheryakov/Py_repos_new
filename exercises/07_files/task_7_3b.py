# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
nvlan = int(input('Введите номер vlan: '))
lst = []

with open('CAM_table.txt', 'r') as src:
    for line in src:
        if line.count('.') is 2:
            a = line.strip('\n').split()
            vlan, mac, _, port = a
            vlan = int(vlan)
            rline = vlan, mac, port
            lst.append(rline)
    lst.sort()
    for ln in lst:
        if nvlan in ln:
            print(ln)