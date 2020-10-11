#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
text = argv[1:]
text = ''.join(text)
ignore = ["duplex", "alias", "Current configuration"]
result_dict = []

with open(text) as lines:
    lines = lines.readlines()
    for line in lines:
        if ignore[0] not in line\
        and ignore[1] not in line\
        and ignore[2] not in line:
            result_dict.append(line)

with open('config_sw1_cleared.txt', 'w') as dest:
    dest.writelines(result_dict)