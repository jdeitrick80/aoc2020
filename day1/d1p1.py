with open('d1p1.in') as f:
  lines = f.read().splitlines()


for i in lines:
	for j in lines:
		if ((int(i) + int(j)) == 2020):
			print(int(i)*int(j))
			break
