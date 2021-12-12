s = '12'
n = 0
L = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for f in s:
                    for g in s:
                        if (a + b + c + d + f + g).count('2') == 2:
                            n += 1
                            L.append(a + b + c + d + f + g)
                            # print(a + b + c + d + f + g)
print(set(L))
