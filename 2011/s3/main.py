from math import pow, floor
a = [[0, 0, 0, 0, 0],
     [1, 2, 0, 0, 0],
     [1, 1, 2, 0, 0],
     [1, 2, 0, 0, 0],
     [0, 0, 0, 0, 0]]
def calc(x, y, m, c):
    cx = int(x/pow(5, m-c))
    cy = int(y/pow(5, m-c))
    # print(cx, cy, pow(5, m-c), lx, ly, pow(5, c-1), pow(5, c-1), c)
    cx = cx%5
    cy = cy%5
    if a[cx][cy] == 1:
        return True
    elif a[cx][cy] == 0:
        return False
    elif c == m:
        return False
    else:
    # if c < m:
        return calc(x, y, m, c+1)
t = int(input())
for i in range(t):
    ip = input().split()
    fm, fx, fy  = map(int, ip)
    if calc(fx, fy, fm, 1):
        print("crystal")
    else:
        print("empty")
