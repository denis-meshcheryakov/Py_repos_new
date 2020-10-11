#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt', 'r') as text:
    ospf = text.readlines()
    for line in ospf:
        line = line.strip().split()
        prefix = line[1]
        ad = line[2].strip('[]')
        n_hop = line[4].rstrip(',')
        l_update = line[5].rstrip(',')
        o_int = line[6]
        result = '''
        Prefix                {0:18}
        AD/Metric             {1:16}
        Next-Hop              {2:16}
        Last update           {3:16}
        Outbound Interface    {4:16}
        '''

        print(result.format(prefix, ad, n_hop, l_update, o_int))