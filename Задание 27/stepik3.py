f = open('27_A (5).txt')
n = int(f.readline())
d = 112
mas = [0] * d
maxsum = 0
ch1 = 0
ch2 = 0
k = 4 #1
buf = [0] * 4
for i in range(k):
    buf[i] = int(f.readline())
for i in range(n - k):
    free = buf[0] #2
    mas[free % d] = max(free,
    mas[free % d])
    noob = int(f.readline()) #3
    inap = (d - (noob % d)) % d
    if mas[inap] > noob:
        if maxsum <= noob + mas[inap]:
            maxsum = noob + mas[inap]
            ch1 = mas[inap]
            ch2 = noob
    del buf[0] #4
    buf.append(noob)
    if ch1 != 0 and ch2 != 0:
        print(ch1, ch2)
print(-1)