#full score in PyPy 3
n = int(input())
m = tuple(map(int, input().split()))
final = []
tab = [[float("inf")]*n for _ in range(n)]
for i in range(n):
    lowest = float("inf")
    for j in range(n-i):
        if i == 0:
            tab[i][j] = 0
            lowest = 0
        elif i == 1:
            tab[i][j] = abs(m[j]-m[j+i])
            if tab[i][j] < lowest:
                lowest = tab[i][j]
        else:
            tab[i][j] = tab[i-2][j+1] + abs(m[j]-m[j+i])
            if tab[i][j] < lowest:
                lowest = tab[i][j]
    final.append(lowest)
print(" ".join(map(str, final)))