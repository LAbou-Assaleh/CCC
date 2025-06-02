#13/15
from collections import defaultdict
import sys
n = int(sys.stdin.readline())
friend = [list(map(int, sys.stdin.readline().split()))for x in range(n)]
l= 0
h = 10**(6)+200000
ans = float("inf")
memo = defaultdict()
mid = 0
def dis(x):
    if x in memo:
        return memo[x]
    s = sum(max(abs(x-p)-d, 0)*w for p, w, d in friend)
    memo[x] = s
    return s
while l <= h:
    mid = (l + h) >> 1
    y = dis(mid)
    if y > dis(mid+1):
        l = mid+1
    elif y > dis(mid-1):
        h = mid-1
    else:
        ans = dis(mid)
        break
print(int(ans))