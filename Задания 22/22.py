# d = 0
for x in range(1,1000):
# for x in range(9999,99,-1):
    l = 0
    m = 1
    z = x
    while x > 0:
        if x % 2 > 0:
            l += x % 13
        else:
            m *= x % 13
        x //= 13
    if l == 4 and m == 7:
        print(z)
        break