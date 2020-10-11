#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
text = argv[1:]
text = ''.join(text)
ignore = ["duplex", "alias", "Current configuration"]

with open(text) as lines:
    lines = lines.readlines()
    for line in lines:
        if '!' not in line\
        and ignore[0] not in line\
        and ignore[1] not in line\
        and ignore[2] not in line:
            print(line)