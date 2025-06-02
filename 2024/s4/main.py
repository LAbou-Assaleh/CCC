import sys
sys.setrecursionlimit(10**6)
n, m = list(map(int, input().split()))
graph = [[] for x in range(n+1)]
visited = [0]*(n+1)
c = ["G"]*m
for i in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append((y, i))
    graph[y].append((x, i))

def dfs(n, col):
    if visited[n]:
        return
    visited[n] = 1
    for i, j in graph[n]:
        if not visited[i]:
            if c[j] == "G":
                if col:
                    c[j] = "R"
                else:
                    c[j] = "B"
            dfs(i, col ^ 1)

for i in range(1, n+1):
    if visited[i]:
        pass
    else:
        dfs(i, 0)
print("".join(c))
