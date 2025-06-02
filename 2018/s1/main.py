n = int(input())
x = []
for i in range(n):
    x.append(int(input()))

least = float("inf")
x.sort()
for i in range(1, n-1):
    l = x[i]-(x[i-1]+x[i])/2
    r = (x[i+1]+x[i])/2-x[i]
    d = l+r
    if d < least:
        least = d
print(round(least, 1))
