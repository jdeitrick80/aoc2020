import re

with open('d2p1.in') as f:
    lines = f.read().splitlines()

good=0

for line in lines:
    match = re.search(r'^(\d+)-(\d+)\s(\w):\s(\w+)', line)
    if(bool(match[4].count(match[3],int(match[1])-1,int(match[1]))) != bool(match[4].count(match[3],int(match[2])-1,int(match[2])))):
        good += 1
print(good, " good passwords")
