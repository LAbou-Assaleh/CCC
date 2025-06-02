x = int(input())
t = set()
a = set()
g = {}
for i in range(x):
    t.add(tuple(input().split()))
y = int(input())
for i in range(y):
    a.add(tuple(input().split()))
temp = int(input())
for i in range(temp):
    p = input().split()
    g[p[0]] = {p[1], p[2]}
    g[p[1]] = {p[0], p[2]}
    g[p[2]] = {p[1], p[0]}
count = 0
for i in t:
    if i[1] not in g[i[0]]:
        count += 1
for i in a:
    if i[1] in g[i[0]]:
        count += 1
print(count)


