for n in range(1000):
    n = n - (n % 4)
    c = str(bin(n).replace('0b', ''))
    for i in range(2):
        if c.count('1') % 2 == 1:
            c = c + '1'
        else:
            c = c + '0'
    f = int(c, 2)
    if f > 56:
        print(f)
        break
