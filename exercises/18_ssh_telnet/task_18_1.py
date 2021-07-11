# -*- coding: utf-8 -*-
"""
Задание 18.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* com_mand - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду com_mand на все устройства из файла dev_ices.yaml с помощью функции send_show_command
(эта часть кода написана).

"""
import yaml
from netmiko import ConnectHandler


def send_show_command(device, commands):
    with ConnectHandler(**device) as ssh:
        result = ssh.send_command(commands)
    return result


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
