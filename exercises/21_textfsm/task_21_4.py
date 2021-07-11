# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* com_mand - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из dev_ices.yaml.
"""
import os
from pprint import pprint
from netmiko import ConnectHandler
import yaml
from task_21_3 import parse_command_dynamic


# def send_and_parse_show_command(device_dict, com_mand, templates_path):
#     if "NET_TEXTFSM" not in os.environ:
#         os.environ["NET_TEXTFSM"] = templates_path
#     with ConnectHandler(**device_dict) as ssh:
#         ssh.enable()
#         output = ssh.send_command(com_mand, use_textfsm=True)
#     return output
#
#
# if __name__ == "__main__":
#     full_pth = os.path.join(os.getcwd(), 'templates')
#     with open('dev_ices.yaml') as f:
#         dev_ices = yaml.safe_load(f)
#     for device in dev_ices:
#         result = send_and_parse_show_command(
#             device, 'sh ip int brie', templates_path=full_pth
#         )
#         pprint(result, width=120)


def send_and_parse_show_command(device_dict, command, template_path, index='index'):
    attributes = {'Command': command, 'Vendor': device_dict['device_type']}
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        parsed_data = parse_command_dynamic(
            output, attributes, templ_path=template_path, index_file=index
        )
    return parsed_data


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), 'templates')
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_and_parse_show_command(device, 'sh ip int br', template_path=full_pth)
        pprint(result, width=120)
