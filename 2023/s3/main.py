s = list("defhijklmnopqrstuvxyz")
x = input().split()
n = int(x[0])
m = int(x[1])
r = int(x[2])
c = int(x[3])
k = 0
def main():
    global s, k
    if r == 0 and c == 0:
        for i in range(n-1):
            print("a"*(m-1)+"b")
        print("g"*(m-1)+"a")
        return
    if r == n or c == m:
        if r == n and c == m:
            for i in range(n):
                print("a"*m)
            return
        if r != 0 and c != 0:
            if (n%2 == 0 and r%2 == 1) or (m%2 == 0 and c%2 == 1):
                print("IMPOSSIBLE")
                return
        if r == n:
            if c%2 == 1:
                for i in range(n-1):
                    print("a"*(c//2)+"b"*(m//2-c//2)+"a"+"b"*(m//2-c//2)+"a"*(c//2))
                print("a" * (c // 2) + "g" * (m // 2 - c // 2) + "a" + "g" * (m // 2 - c // 2) + "a" * (c // 2))
                return
            else:
                for i in range(n-1):
                    print("a"*(c//2)+"b"*(m-c)+"a"*(c//2))
                print("a" * (c // 2) + "g" * (m - c) + "a" * (c // 2))
                return
        if c == m:
            if r %2 == 0:
                for i in range(n):
                    if i < r//2 or i > n-r//2-1:
                        print("a"*m)
                    else:
                        print("b"*(m-1)+"g")
                return
            else:
                for i in range(n):
                    if i < r//2 or i > n-r//2-1:
                        print("a"*m)
                    elif i == n//2:
                        print("a"*m)
                    else:
                        print("b"*(m-1)+"g")
                return

    if r == 0:
        for i in range(n):
            txt = ""
            k = 0
            for z in range(m):
                if z < c:
                    txt += s[k % len(s)]
                elif i == n-1:
                    txt += "w"
                else:
                    txt += "g"
                k += 1
                if k > len(s):
                    k = 0
            print(txt)
        return
    if c == 0:
        for i in range(n):
            txt = ""
            if i < r:
                txt += s[k % len(s)]*m
            else:
                txt += "w"*(m-1)+"g"
            k += 1
            if k > len(s):
                k = 0
            print(txt)
        return
    grid = []
    for k in range(n):
        grid.append(["a"]*m)
    for i in range(m):
        for z in range(n):
            if i < c:
                grid[z][i] = "b"
            else:
                grid[z][i] = s[k%len(s)]
                k += 1
    for j in range(n):
        if j < r:
            print("b"*m)
        else:
            print("".join(grid[j]))
main()