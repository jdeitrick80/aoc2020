with open('d9p1.in') as f:
    lines = f.read().splitlines()

preamble_len=25
count=0

data = lines[(count+preamble_len):len(lines)]

for entry in data:
	preamble = lines[count:(count+preamble_len)]
	valid=0
	for i in preamble:
		for j in preamble:
			if ((int(i) + int(j)) == int(entry)):
				valid = 1
				break
		if(valid==1):
			break
	if(valid==0):
		print(f"{entry} is invalid")
		break
	else:
		count+=1

