import numpy as np

with open('d9p1.in') as f:
    lines = f.read().splitlines()

preamble_len=25
count=0

invalid=0

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
		invalid=int(entry)
		break
	else:
		count+=1

print(f"{invalid} is invalid")

count = 0
for i in lines:
	count+=1
	rest=lines[count:len(lines)]
	contig=[int(i)]
	for j in rest:
		contig.append(int(j))
		if(sum(contig)==invalid):
			print((min(contig)+max(contig)))
			break
		

