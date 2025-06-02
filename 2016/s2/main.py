q = input()
n = int(input())
d = input().split()
p = input().split()
d = [int(x) for x in d]
p = [int(x) for x in p]
speed = 0
d.sort()
p.sort()
if q == '2':
    for i in range(n):
        if d[i] > p[n-i-1]:
            speed += d[i]
        else:
            speed += p[n-i-1]
else:
    for i in range(n):
        if d[i] > p[i]:
            speed += d[i]
        else:
            speed += p[i]
print(speed)