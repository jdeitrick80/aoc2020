with open('d3p1.in') as f:
    lines = f.read().splitlines()

xmax = len(lines[0])
ymax = len(lines)

x = 0
y = 0
product = 1

slopes = [3,1],

trees = 0

while y < ymax:
    if (lines[y].count('#', x, x+1)):
        trees += 1
    x = (x + 3) % xmax
    y += 1

print(trees)


