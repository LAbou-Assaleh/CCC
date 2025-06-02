p = int(input())
s = input().split()
s = [float(x) for x in s]
w = input().split()
w = [float(x) for x in w]
area = 0
for i in range(p):
    area += w[i]*(s[i]+s[i+1])/2
print(area)