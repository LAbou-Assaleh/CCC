a = input()
b = input()
c = input()
d = input()
over = True
if a == "8" or a == "9":
    if b == c:
        if d == "8" or d == "9":
            print("ignore")
            over = False
if over:
    print("answer")