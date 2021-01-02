with open('d3p1.in') as f:
	lines = f.read().splitlines()

xmax = len(lines[0])
ymax = len(lines)

product = 1

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for row in slopes: 
	x = 0
	y = 0
	trees = 0
	while y < ymax:
		if (lines[y].count('#', x, x+1)):
			trees += 1
		x = (x + row[0]) % xmax
		y += row[1]

	print(trees)
	product *= trees

print(product)
