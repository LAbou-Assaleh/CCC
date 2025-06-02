n = int(input())
tiles = []
tn = 0
next = 0
for i in range(2):
    p = input().split()
    tiles.append(p)
for i in range(2):
    for j in range(n):
        if tiles[i][j] == "1":
            tn += 1
for i in range(2):
    for j in range(1, n):
        if tiles[i][j] == "1":
            if tiles[i][j-1] == "1":
                next += 2
for j in range(n):
    if (j+1)%2 != 0:
        if tiles[1][j] == "1":
            if tiles[0][j] == "1":
                next += 2
print(tn*3-next)
