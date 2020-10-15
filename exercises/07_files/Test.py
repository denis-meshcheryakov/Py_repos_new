with open('CAM_table.txt', 'r') as start:
    lists = []
    for line in start:
        if line.count('.') is 2:
            a = line.strip('\n').split()
            a.pop(-2)
            lists.append(a)
    lists.sort()
    for l in lists:
        print(l[0] + '    ' + l[1] + '   ' + l[2])