n = input()
x = n.count("H")
y = n.count("V")
grid = [["1", "2"],
        ["3", "4"]]
if x%2 == 1:
    grid = [grid[1], grid[0]]
if y%2 == 1:
    grid[0] = [grid[0][1], grid[0][0]]
    grid[1] = [grid[1][1], grid[1][0]]

for i in grid:
    print(" ".join(i))