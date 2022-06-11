s = open('24-j6 (1).txt').readline()
k = 1
count = 0
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        k += 1
    else:
        if k == 5:
            count += 1
        k = 1
print(count)