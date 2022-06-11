for x in range(100,1000):
    s = x
    l = x
    m = 81
    if l % 2 == 1:
        m = 30
    while l != m:
        if l > m:
            l -= m
        else:
            m -= l
    if m == 15:
        print(s)
        break