#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""


from tabulate import tabulate
import task_12_1


def print_ip_table(reach_list, unreach_list):
    src = {'Reachable': reach_list, 'Unreachable': unreach_list}
    print(tabulate(src, headers='keys'))


if __name__ == "__main__":
    reach_list = ['10.1.1.1', '10.1.1.2 ']
    unreach_list = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
    print_ip_table(reach_list, unreach_list)
