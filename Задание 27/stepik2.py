with open('27_B (2).txt') as f:
    n = int(f.readline())
    k = 9
    buf = [0] * k
    maxch = 0
    maxnch = 0
    maxpr = 0

    for i in range(k):
        buf[i] = int(f.readline())

    for i in range(n-k):
        free = buf[0]
        if free % 2 == 0:
            maxch = max(maxch, free)
        else:
            maxnch = max(maxnch, free)
        noob = int(f.readline())
        if noob % 2 == 0:
            maxpr = max(maxpr, max(maxnch, maxch) * noob)
        else:
            maxpr = max(maxpr, maxch * noob)
        del buf[0]
        buf.append(noob)
print(maxpr)