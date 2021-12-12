# s = '1' * 70
#
# while '1111' in s or '2222' in s:
#
#     if '1111' in s:
#         s = s.replace('1111', '22')
#     else:
#         s = s.replace('2222', '11')
# print(s)



a = 10 ** 2019 - 10 ** 1019 + 10 ** 1200 - 10 ** 3
s = str(a).count('9')
print(s)