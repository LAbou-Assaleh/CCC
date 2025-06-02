n = int(input())
d = [[], [], [], [], []]
for i in range(n):
    s = input()
    for i in range(5):
        if s[i] == "Y":
            d[i].append(1)
check = 0
for i in range(5):
    d[i] = len(d[i])
    if d[i] > check:
        check = d[i]
string = ""
for i in range(5):
    if d[i] == check:
        string += str(i+1) + ","
print(string[:-1])