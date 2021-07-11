# -*- coding: utf-8 -*-
"""
Задание 21.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 21.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""
from task_21_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command, device, command, templates_path)
            for device in devices
        ]
        output = {device['host']: f.result() for device, f in zip(devices, result_all)}
    return output


if __name__ == "__main__":
    with open('devices.yaml') as f:
        dev_ices = yaml.safe_load(f)
    com_mand = 'sh ip int br'
    path_dir = f'{os.getcwd()}/templates'
    pprint(send_and_parse_command_parallel(dev_ices, com_mand, path_dir))
