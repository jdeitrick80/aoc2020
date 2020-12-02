with open('d1p1.in') as f:
  lines = f.read().splitlines()


found = 0

for i in lines:
	for j in lines:
		for k in lines:
			if ((int(i) + int(j) + int(k)) == 2020):
				found = int(i)*int(j)*int(k)
				print(found)
				break
		if found:
			break
	if found:
		break
