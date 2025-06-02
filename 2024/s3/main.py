# def solve():
#     print("YES")
#     return
l = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
b2 = []
t = []
left = 0
v = b[0]
for i in range(l):
    if v == b[i]:
        pass
    else:
        b2.append(b[i-1])
        t. append((left, i-1))
        v = b[i]
        left = i
b2.append(b[i])
t. append((left, i))
L = []
R = []
c = 0
for i in range(l):
    if c == len(b2):
        break
    if a[i] == b2[c]:
        if t[c][0]<i:
            L.append((t[c][0], i))
        if t[c][1]>i:
            R.append((i, t[c][1]))
        c += 1
if c == len(b2) and c != l:
    print("YES")
    print(len(R)+len(L))
    for i in range(len(R)-1, -1, -1):
        print(f"R {R[i][0]} {R[i][1]}")
    for i in range(len(L)):
        print(f"L {L[i][0]} {L[i][1]}")
else:
    if a == b:
        print("YES")
        print(0)
    else:
        print("NO")
