d = {}
mmax = 0
for x in range(200, 250):
    s = '1' * x

    while ('111' in s) or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    mmax = max(mmax, s.count('1'))

    d[x] = s.count('1')

for i in d:
    if d[i] == mmax:
        print(i)




