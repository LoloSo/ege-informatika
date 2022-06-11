# strok = int(f'12345576')
# if strok % 8 == 0:
#     print(strok, strok//8)
# for i in range(0,10):
#     strok = int(f'1234557{i}6')
#     if strok % 8 == 0:
#         print(strok, strok//8)
for x in range(1,5000):
    for y in range(1,5000):
        if (x * x) + (y * y) == 1945:
            print(x,y)