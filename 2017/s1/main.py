import sys

n = int(input())
t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
k = n
t1.reverse()
t2.reverse()
t1s = sum(t1)
t2s = sum(t2)
for i in range(n):
    if t1s == t2s:
        print(k)
        sys.exit()
    else:
        t1s -= t1[i]
        t2s -= t2[i]
    k -= 1
print(0)


