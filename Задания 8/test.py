s = 'ШАР'
n = 0
for a in s:
    for b in s:
        for c in s:
            if (a + b + c).count('Р') == 1:
                n += 1
print(n)