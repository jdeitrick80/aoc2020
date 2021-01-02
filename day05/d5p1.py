with open('d5p1.in') as f:
	lines = f.read().splitlines()

maxnum = 0

for ticket in lines:
	ticket = ticket.replace('F','0')
	ticket = ticket.replace('B','1')
	ticket = ticket.replace('L','0')
	ticket = ticket.replace('R','1')

	idnum = int(ticket,2)

	if (idnum > maxnum):
		maxnum = idnum

print(maxnum)
