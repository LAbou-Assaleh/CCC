num = int(input())
list = []
for i in range(num):
    list.append(input().split())
list = [[int(i) for i in j] for j in list]
def rotate(list):
    l = []
    for i in range(num-1, -1, -1):
        temp = []
        for j in range(num):
            temp.append(list[j][i])
        l.append(temp)
    return l
# def rotateback(list):
#     l = []
#     for i in range(num):
#         temp = []
#         for j in range(num):
#             temp.append(list[j][i])
#         l.append(temp)
#     return l
for i in range(4):
    go = True
    for i in range(1, num):
        if list[i][0] < list[i - 1][0]:
            go = False
        for j in range(1, num):
            if list[i][j] < list[i - 1][j]:
                go = False
            if list[i][j] < list[i][j-1]:
                go = False
    if go:
        for i in range(num):
            string = ""
            for j in range(num):
                string += str(list[i][j]) + " "
            print(string[:-1])
        break
    else:
        list = rotate(list)