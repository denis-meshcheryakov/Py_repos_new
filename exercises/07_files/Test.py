a = ['Current configuration : 2033 bytes',
'!',
'service timestamps debug datetime msec',
'interface Ethernet0/0',
'duplex auto',
'alias configure sh do sh ']

ignore = ["duplex", "alias", "Current configuration"]

for line in a:
    if '!' not in line\
    and ignore[0] not in line\
    and ignore[1] not in line\
    and ignore[2] not in line:
        print(line)
