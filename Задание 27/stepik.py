with open('27_A (3).txt') as file:
    n = int(file.readline())
    k = 7
    buf = [0] * k
    maxs = 0
    for i in range(k):
        buf[i] = int(file.readline())

    for i in range(n - k):
        free = buf[0]
        noob = int(file.readline())
        maxs =max(maxs, free+noob)
        del buf[0]
        buf.append(noob)
print(maxs)