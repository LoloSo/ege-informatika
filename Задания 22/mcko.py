
for x in range(10000, 1, -1):
    Q = 15
    L = 0
    C = x
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 3 and M == 7:
        print(C)