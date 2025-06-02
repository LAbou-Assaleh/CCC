import heapq
from collections import defaultdict
m, n = list(map(int, input().split()))
adj = defaultdict(list)
r = []
for i in range(n):
    x, y, l, c = list(map(int, input().split()))
    r.append([x, y, l ,c])

r.sort(key=lambda x:(x[2], x[3]))
def dijrkstra(start, end, target):
    d = defaultdict(lambda :float("inf"))
    d[start] = 0
    pq = [(0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > d[node]:
            continue
        if node == end:
            break
        for i, distance in adj[node]:
            if dist + distance < d[i]:
                heapq.heappush(pq,(dist+distance, i))
                d[i] = dist + distance
    return True if d[end] <= target else False
cost = 0
for i in r:
    if not dijrkstra(i[0], i[1], i[2]):
        cost+=i[3]
        adj[i[0]].append([i[1],i[2]])
        adj[i[1]].append([i[0], i[2]])

print(cost)