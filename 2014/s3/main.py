def clear(m, l , b):
    while True:
        if b != []:
            if b[-1] == l[-1]+1:
                x = b.pop(-1)
                l.append(x)
                continue
            elif m == []:
                print("N")
                return
            elif m[-1] == l[-1]+1:
                x = m.pop(-1)
                l.append(x)
                continue
            else:
                x = m.pop(-1)
                b.append(x)
                continue
        elif m != []:
            if m[-1] == l[-1] + 1:
                x = m.pop(-1)
                l.append(x)
                continue
            else:
                x = m.pop(-1)
                b.append(x)
                continue
        else:
            print("Y")
            return
t = int(input())
for i in range(t):
    n = int(input())
    m = []
    l = [0]
    b = []
    for j in range(n):
        x = int(input())
        m.append(x)
    clear(m , l, b)

