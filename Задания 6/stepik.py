for x in range(1,1000):
    for s in range(1,1000):
        q = x
        s = 100 * s + x
        n = 1
        while s < 2021:
            s = s + 5 * n
            n = n + 1
        if n == 17:
            print(q)