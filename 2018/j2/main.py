num = input()
l1 = input()
l2 = input()
count = 0
for i in range(int(num)):
    if l1[i] == "C" and l2[i] == "C":
        count += 1
print(count)