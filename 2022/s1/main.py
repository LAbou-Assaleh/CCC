import math


n = int(input())
count = 0
for i in range(math.ceil(n/5)+1):
    x = n-5*i
    if x < 0:
        continue
    if (x/4).is_integer():
        count += 1
print(count)