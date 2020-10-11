#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv
src = argv[1]
src = ''.join(src)
dest = argv[2]
dest = ''.join(dest)
ignore = ["duplex", "alias", "Current configuration"]
result_dict = []

with open(src) as lines:
    lines = lines.readlines()
    for line in lines:
        if ignore[0] not in line\
        and ignore[1] not in line\
        and ignore[2] not in line:
            result_dict.append(line)

with open(dest, 'w') as des_t:
    des_t.writelines(result_dict)