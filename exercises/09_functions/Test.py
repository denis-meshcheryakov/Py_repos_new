ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)
def get_config(config):
    config_dict = {}
    with open(config, 'r') as file:
        for line in file:
            if ignore_command(line, ignore) or line.find('!') != -1:
                continue
            else:
                if line.startswith(' '):
                    slave = line.strip()
                    config_dict[main].append(slave)
                else:
                    main = line.strip()
                    config_dict[main] = []
    return config_dict
print(get_config('config_sw1.txt'))