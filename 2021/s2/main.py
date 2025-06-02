# 10/15
c = int(input())
r = int(input())
k = int(input())
x = 0
canvas = [[0 for x in range(r)] for x in range(c)]
for i in range(k):
    sub = input().split()
    if sub[0] == "R":
        for j in range(r):
            if canvas[int(sub[1])-1][j] == 0:
                canvas[int(sub[1])-1][j] = 1
                x += 1
            else:
                canvas[int(sub[1])-1][j] = 0
                x -= 1
    if sub[0] == "C":
        for l in range(c):
            if canvas[l][int(sub[1])-1] == 0:
                canvas[l][int(sub[1])-1] = 1
                x += 1
            else:
                canvas[l][int(sub[1])-1] = 0
                x -= 1
print(x)