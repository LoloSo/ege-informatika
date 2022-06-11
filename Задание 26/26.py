# n = 90500
# s = 0
# k = 0
# b = 0
# with open('26.txt') as file:
#     lst = sorted(list(map(int, file.readlines())))
# for i in range(len(lst)):
#     if lst[i] > 3000:
#         s += lst[i]
#         k += 1
#         b = lst[i-1]
#         print(b)
#     if k == 3:
#         break
# for j in range(len(lst)):
#     if s + lst[j] > 90500:
#         break
#     else:
#         k += 1
#         s += lst[j]
#         print(lst[j])
#
# print(k)
# a = [1,1,2,3]
# a = list(set(a))
# a.remove(2)
# print(a)

f = open('26-k6 (1).txt')
n, k = map(int, f.readline().split())
weight, cost = [0]*n, [0]*n
for i in range(n):
    weight[i], cost[i] = map(int, f.readline().split())
for i in range(n-1):
    for j in range(i+1, n):
        if cost[i]/weight[i] > cost[j]/weight[j] or cost[i]/weight[i] == cost[j]/weight[j] and weight[i] < weight[j]:
            cost[i], cost[j] = cost[j], cost[i]
            weight[i], weight[j] = weight[j], weight[i]
w = weight[0]
c = cost[0]
for i in range(1, k):
    if weight[i] > w:
        w = weight[i]
        c = cost[i]
print(sum(weight[0:k]), w)