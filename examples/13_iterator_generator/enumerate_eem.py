import sys

config = sys.argv[1]

with open(config, 'r') as file:
    for (i, command) in enumerate(file, 1):
        print('action {:04} cli com_mand "{}"'.format(i, command.rstrip()))
