r1 = input().split()
r2 = input().split()
r3 = input().split()
r = [r1, r2, r3]
xs = r[0].count("X") + r[1].count("X") + r[2].count("X")

def base(ox):
    for i in range(3):
        if r[i][0] == "X" and not r[i][1].isalpha() and not r[i][2].isalpha():
            r[i][0] = str(int(r[i][1])-(int(r[i][2])-int(r[i][1])))
        if r[i][1] == "X" and not r[i][0].isalpha() and not r[i][2].isalpha():
            r[i][1] = str(int(int(r[i][0])+(int(r[i][2])-int(r[i][0]))/2))
        if r[i][2] == "X" and not r[i][1].isalpha() and not r[i][0].isalpha():
            r[i][2] = str(int(r[i][1])+int(r[i][1])-int(r[i][0]))
        if r[0][i] == "X" and not r[1][i].isalpha() and not r[2][i].isalpha():
            r[0][i] = str(int(r[1][i])-(int(r[2][i])-int(r[1][i])))
        if r[1][i] == "X" and not r[0][i].isalpha() and not r[2][i].isalpha():
            r[1][i] = str(int(int(r[0][i])+(int(r[2][i])-int(r[0][i]))/2))
        if r[2][i] == "X" and not r[0][i].isalpha() and not r[1][i].isalpha():
            r[2][i] = str(int(r[1][i]) + int(r[1][i]) - int(r[0][i]))
    xs = r[0].count("X") + r[1].count("X") + r[2].count("X")
    if ox == xs:
        return
    else:
        base(xs)
def allin():
    global r
    if xs == 8:
        for i in r:
            for j in i:
                if not j.isalpha():
                    r = [[j]*3]*3
                    return

    if xs == 9:
        r = [["0"]*3]*3
        return
    if xs == 7:
        for i in range(3):
            if r[i][0] == "X" and not r[i][1].isalpha() and not r[i][2].isalpha():
                r[i][0] = str(int(r[i][1]) - (int(r[i][2]) - int(r[i][1])))
            if r[i][1] == "X" and not r[i][0].isalpha() and not r[i][2].isalpha():
                r[i][1] = str(int(int(r[i][0]) + (int(r[i][2]) - int(r[i][0])) / 2))
            if r[i][2] == "X" and not r[i][1].isalpha() and not r[i][0].isalpha():
                r[i][2] = str(int(r[i][1]) + int(r[i][1]) - int(r[i][0]))
            if r[0][i] == "X" and not r[1][i].isalpha() and not r[2][i].isalpha():
                r[0][i] = str(int(r[1][i]) - (int(r[2][i]) - int(r[1][i])))
            if r[1][i] == "X" and not r[0][i].isalpha() and not r[2][i].isalpha():
                r[1][i] = str(int(int(r[0][i]) + (int(r[2][i]) - int(r[0][i])) / 2))
            if r[2][i] == "X" and not r[0][i].isalpha() and not r[1][i].isalpha():
                r[2][i] = str(int(r[1][i]) + int(r[1][i]) - int(r[0][i]))

        for i in range(3):
            for j in range(3):
                if not r[i][j].isalpha():
                    r[i] = [r[i][j]]*3

        for i in range(3):
            if r[i][0] == "X" and not r[i][1].isalpha() and not r[i][2].isalpha():
                r[i][0] = str(int(r[i][1]) - (int(r[i][2]) - int(r[i][1])))
            if r[i][1] == "X" and not r[i][0].isalpha() and not r[i][2].isalpha():
                r[i][1] = str(int(int(r[i][0]) + (int(r[i][2]) - int(r[i][0])) / 2))
            if r[i][2] == "X" and not r[i][1].isalpha() and not r[i][0].isalpha():
                r[i][2] = str(int(r[i][1]) + int(r[i][1]) - int(r[i][0]))
            if r[0][i] == "X" and not r[1][i].isalpha() and not r[2][i].isalpha():
                r[0][i] = str(int(r[1][i]) - (int(r[2][i]) - int(r[1][i])))
            if r[1][i] == "X" and not r[0][i].isalpha() and not r[2][i].isalpha():
                r[1][i] = str(int(int(r[0][i]) + (int(r[2][i]) - int(r[0][i])) / 2))
            if r[2][i] == "X" and not r[0][i].isalpha() and not r[1][i].isalpha():
                r[2][i] = str(int(r[1][i]) + int(r[1][i]) - int(r[0][i]))
            return
base(xs)
xs = r[0].count("X") + r[1].count("X") + r[2].count("X")
while xs != 0:
    if xs < 4 and xs > 0:
        base(xs)
    if xs >= 4:
        if r[1][1] == "X":
            r[1][1] = "0"
        elif r[1][0] == "X":
            r[1][0] = "0"
        elif r[1][2] == "X":
            r[1][2] = "0"
        elif r[0][1] == "X":
            r[0][1] = "0"
        elif r[2][1] == "X":
            r[2][1] = "0"
        else:
            r[0][0] = "0"
        base(xs)

    xs = r[0].count("X") + r[1].count("X") + r[2].count("X")
for i in r:
    print(" ".join(i))
