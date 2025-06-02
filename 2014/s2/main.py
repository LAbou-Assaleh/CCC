n = int(input())
x = input().split()
y = input().split()
index = {}
for i in range(n):
    index[x[i]] = y[i]
stop = False
for x in index.keys():
    if x != index[index[x]] or x == index[x]:
        print("bad")
        stop = True
        break
if not stop:
    print("good")