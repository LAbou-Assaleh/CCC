temp = input().split()
n = int(temp[0])
l = int(temp[1])
d = set()
for i in range(n):
    go = True
    d.clear()
    s = list(input())
    v = set()
    for j in s:
        if j in v:
            d.add(j)
        else:
            v.add(j)
    for k in range(1, l):
        if s[k] not in d:
            if s[k-1] not in d:
                go = False
        if s[k] in d:
            if s[k-1] in d:
                go = False
    if go:
        print("T")
    else:
        print("F")
