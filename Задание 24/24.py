with open('24 (9).txt') as f:
    f = f.readline()
    f = f.replace('AB', '**')
    f = f.replace('AD', '**')
    dlina = 0
    maxdl = 0
    for i in range(len(f)):
        if f[i] == '*':
            dlina += 1
        else:
            maxdl = max(maxdl, dlina)
            dlina = 0
print(maxdl)