n = int(input()); p1 = [];count = 0
for i in range(n//2):p1.append(input())
for i in range(n//2):
    p = input()
    if p == p1[i]:count += 2
print(count)