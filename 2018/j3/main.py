citys = input().split()
citys = ["0"] + citys
string = "0 "
for i in range(1, len(citys)):
    citys[i] = int(citys[i]) + int(citys[i-1])
    string += str(citys[i])
    string += " "
print(string[:-1])
for i in range(1, len(citys)):
    string = ""
    for j in range(len(citys)):
        if i > j:
            string += str(abs(int(citys[j]) - int(citys[i])))
        elif i == j:
            string += "0"
        elif i < j:
            string += str(abs(int(citys[j]) - int(citys[i])))
        string += " "
    print(string[:-1])

